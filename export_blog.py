import os
import re
import sys
import json
import time
import urllib.parse
import urllib3
import requests
from bs4 import BeautifulSoup
import html2text

urllib3.disable_warnings()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'backup_data')
POSTS_DIR = os.path.join(OUTPUT_DIR, 'posts')
IMAGES_DIR = os.path.join(OUTPUT_DIR, 'images')
RAW_HTML_DIR = os.path.join(OUTPUT_DIR, 'raw_html')

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(RAW_HTML_DIR, exist_ok=True)

# Cookie for fetching private/hidden posts
COOKIE = os.environ.get('TISTORY_COOKIE', '').strip()

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

if COOKIE:
    HEADERS['Cookie'] = COOKIE

def get_post_urls():
    # If cookie is present, probe IDs 1 to 150 to catch private posts too
    if COOKIE:
        print("Using provided Cookie header to discover private posts...")
        urls = []
        for i in range(1, 150):
            urls.append(f"https://priv.tistory.com/{i}")
        return urls
    else:
        sitemap_url = 'https://priv.tistory.com/sitemap.xml'
        resp = requests.get(sitemap_url, headers=HEADERS, verify=False, timeout=10)
        locs = re.findall(r'<loc>(.*?)</loc>', resp.text)
        post_urls = [loc for loc in locs if re.search(r'priv\.tistory\.com/\d+$', loc)]
        def get_id(u):
            m = re.search(r'/(\d+)$', u)
            return int(m.group(1)) if m else 0
        post_urls.sort(key=get_id)
        return post_urls

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = name.strip().replace(' ', '_')
    return name[:60]

def download_image(img_url, post_id, img_index):
    try:
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        parsed = urllib.parse.urlparse(img_url)
        ext = os.path.splitext(parsed.path)[1]
        if not ext or len(ext) > 5:
            ext = '.png'
        
        filename = f"img_{post_id}_{img_index:02d}{ext}"
        filepath = os.path.join(IMAGES_DIR, filename)

        if not os.path.exists(filepath):
            resp = requests.get(img_url, headers=HEADERS, verify=False, timeout=15)
            if resp.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(resp.content)
        return f"../images/{filename}"
    except Exception as e:
        print(f"Failed to download image {img_url}: {e}")
        return img_url

def parse_post(url):
    post_id = url.split('/')[-1]
    resp = requests.get(url, headers=HEADERS, verify=False, timeout=10)
    if resp.status_code != 200:
        print(f"[{post_id}] Skipped (Status code {resp.status_code})")
        return None

    html = resp.text
    # Save raw html
    with open(os.path.join(RAW_HTML_DIR, f"{post_id}.html"), 'w', encoding='utf-8') as f:
        f.write(html)

    soup = BeautifulSoup(html, 'html.parser')

    # Check if redirected to login page or access denied page
    if "로그인이 필요" in html or "권한이 없습니다" in html:
        print(f"[{post_id}] Access Denied (Private post - Cookie required)")
        return None

    # Title
    tit_el = soup.select_one('.tit_post, .title_post, h3.tit_post, .post-cover h1, .h3')
    title = tit_el.text.strip() if tit_el else f"Post {post_id}"

    # Category
    cat_el = soup.select_one('.tit_category, .category_post, .txt_category')
    category = cat_el.text.strip() if cat_el else "카테고리 없음"

    # Date
    meta_date = soup.find('meta', property='article:published_time')
    date_str = meta_date.get('content') if meta_date else ""
    if not date_str:
        date_el = soup.select_one('.txt_detail, .date, .txt_date')
        date_str = date_el.text.strip() if date_el else ""

    # Tags
    tags = []
    desc_tag = soup.select_one('dd.desc_tag, .area_tag, .box_tag, .tag_content')
    if desc_tag:
        raw_tags = desc_tag.text.replace('TAG', '').strip()
        if ',' in raw_tags:
            tags = [t.strip() for t in raw_tags.split(',') if t.strip()]
        else:
            tags = [t.strip() for t in raw_tags.split() if t.strip()]

    # Content
    content_el = soup.select_one('.tt_article_useless_p_margin, .article_view, .entry-content, .contents_style')
    if not content_el:
        content_el = soup.find('body')

    # Process images inside content
    img_index = 1
    for img in content_el.find_all('img'):
        src = img.get('src') or img.get('data-url') or img.get('data-filename')
        if src:
            local_rel_path = download_image(src, post_id, img_index)
            img['src'] = local_rel_path
            img_index += 1

    # Format codeblocks
    for pre in content_el.find_all('pre'):
        lang = pre.get('data-ke-language', '')
        code_content = pre.get_text()
        pre.string = f"\n``` {lang}\n{code_content}\n```\n"

    # Remove unwanted scripts and styling
    for un in content_el.find_all(['script', 'style', 'iframe', 'ins']):
        un.decompose()

    # Convert to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    markdown_content = h.handle(str(content_el))

    # Clean double escaped markdown fences
    markdown_content = re.sub(r'``` (.*?)\n', r'```\1\n', markdown_content)

    return {
        'id': post_id,
        'title': title,
        'category': category,
        'date': date_str,
        'tags': tags,
        'url': url,
        'markdown': markdown_content,
        'html': str(content_el)
    }

def main():
    print("Starting blog export from https://priv.tistory.com...")
    urls = get_post_urls()
    print(f"Targeting {len(urls)} post URLs.")

    knowledge_base = []

    for idx, url in enumerate(urls, 1):
        post_id = url.split('/')[-1]
        print(f"[{idx}/{len(urls)}] Processing post {post_id}: {url}")
        post_data = parse_post(url)
        if not post_data:
            continue

        # Save individual markdown file
        safe_title = sanitize_filename(post_data['title'])
        filename = f"{post_id}_{safe_title}.md"
        filepath = os.path.join(POSTS_DIR, filename)

        frontmatter = f"""---
title: "{post_data['title']}"
date: "{post_data['date']}"
category: "{post_data['category']}"
tags: {json.dumps(post_data['tags'], ensure_ascii=False)}
original_url: "{post_data['url']}"
tistory_id: {post_data['id']}
---

"""
        full_file_content = frontmatter + post_data['markdown']
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_file_content)

        post_data['file_path'] = os.path.relpath(filepath, OUTPUT_DIR)
        knowledge_base.append(post_data)

        time.sleep(0.1)

    # Save aggregated JSON Knowledge Base
    kb_json_path = os.path.join(OUTPUT_DIR, 'knowledge_base.json')
    with open(kb_json_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=2)

    # Save summary Markdown Knowledge Index
    kb_index_path = os.path.join(OUTPUT_DIR, 'INDEX.md')
    with open(kb_index_path, 'w', encoding='utf-8') as f:
        f.write(f"# Blog Knowledge Base Index ({len(knowledge_base)} Posts)\n\n")
        f.write(f"Source: https://priv.tistory.com\n\n")
        f.write("| ID | Category | Title | Date | Tags | File |\n")
        f.write("|---|---|---|---|---|---|\n")
        for item in knowledge_base:
            t_str = ", ".join(item['tags']) if item['tags'] else "-"
            f.write(f"| {item['id']} | {item['category']} | [{item['title']}](./posts/{os.path.basename(item['file_path'])}) | {item['date'][:10]} | {t_str} | [MD](./posts/{os.path.basename(item['file_path'])}) |\n")

    print("\n Export completed successfully!")
    print(f"Downloaded total posts: {len(knowledge_base)}")
    print(f"Posts saved in: {POSTS_DIR}")
    print(f"Images saved in: {IMAGES_DIR}")
    print(f"Knowledge Base JSON: {kb_json_path}")

if __name__ == '__main__':
    main()
