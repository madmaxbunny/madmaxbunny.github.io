import os
import re
import json
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = os.path.join(BASE_DIR, 'backup_data')
KB_JSON_PATH = os.path.join(BACKUP_DIR, 'knowledge_base.json')

POSTS_DIR = os.path.join(BASE_DIR, '_posts')
ASSETS_IMG_DIR = os.path.join(BASE_DIR, 'assets', 'img', 'posts')

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(ASSETS_IMG_DIR, exist_ok=True)

def sanitize_slug(text):
    text = re.sub(r'[^\w\s-]', '', text, flags=re.UNICODE)
    text = re.sub(r'[\s_]+', '-', text).strip('-').lower()
    return text[:40] if text else 'post'

def parse_date(date_str):
    if not date_str:
        return "2024-01-01 00:00:00 +0900", "2024-01-01"
    
    # Try ISO 8601 parsing e.g. 2009-03-09T14:47:41+09:00
    try:
        dt = datetime.fromisoformat(date_str)
        formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S +0900")
        day_str = dt.strftime("%Y-%m-%d")
        return formatted_date, day_str
    except Exception:
        pass

    # Try matching YYYY. MM. DD or YYYY-MM-DD
    m = re.search(r'(\d{4})[.-]\s*(\d{1,2})[.-]\s*(\d{1,2})', date_str)
    if m:
        y, mm, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        dt = datetime(y, mm, d)
        formatted_date = dt.strftime("%Y-%m-%d 00:00:00 +0900")
        day_str = dt.strftime("%Y-%m-%d")
        return formatted_date, day_str

    return "2024-01-01 00:00:00 +0900", "2024-01-01"

def process_categories(cat_str):
    if not cat_str or cat_str == "카테고리 없음":
        return ["기타"]
    parts = [c.strip() for c in cat_str.split('/') if c.strip()]
    # Chirpy supports max 2 level categories
    return parts[:2]

def process_tags(tags_list):
    clean_tags = []
    for t in tags_list:
        t_clean = re.sub(r'[^\w\s-]', '', t, flags=re.UNICODE).strip().lower()
        if t_clean and t_clean not in clean_tags:
            clean_tags.append(t_clean)
    return clean_tags

def convert():
    print("Converting backup data to Jekyll Chirpy posts format...")

    # Copy images to assets/img/posts/
    backup_img_dir = os.path.join(BACKUP_DIR, 'images')
    if os.path.exists(backup_img_dir):
        for img in os.listdir(backup_img_dir):
            src_p = os.path.join(backup_img_dir, img)
            dst_p = os.path.join(ASSETS_IMG_DIR, img)
            shutil.copy2(src_p, dst_p)
        print(f"Copied {len(os.listdir(backup_img_dir))} images to assets/img/posts/")

    with open(KB_JSON_PATH, 'r', encoding='utf-8') as f:
        posts = json.load(f)

    used_filenames = set()

    for item in posts:
        pid = item['id']
        title = item['title']
        raw_date = item['date']
        raw_cat = item['category']
        raw_tags = item['tags']
        markdown = item['markdown']

        formatted_date, day_str = parse_date(raw_date)
        categories = process_categories(raw_cat)
        tags = process_tags(raw_tags)

        # Update image links in markdown
        # replace ../images/ -> /assets/img/posts/
        markdown = markdown.replace('../images/', '/assets/img/posts/')

        # Generate filename YYYY-MM-DD-slug.md
        slug = sanitize_slug(title)
        filename = f"{day_str}-{pid}-{slug}.md"
        
        # Ensure unique filename
        counter = 1
        while filename in used_filenames:
            filename = f"{day_str}-{pid}-{slug}-{counter}.md"
            counter += 1
        used_filenames.add(filename)

        # Create Chirpy Frontmatter
        frontmatter = f"""---
title: "{title.replace('"', '\\"')}"
date: {formatted_date}
categories: {json.dumps(categories, ensure_ascii=False)}
tags: {json.dumps(tags, ensure_ascii=False)}
---

"""
        post_path = os.path.join(POSTS_DIR, filename)
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + markdown)

    print(f"Successfully converted {len(posts)} posts into _posts/ directory for Jekyll Chirpy!")

if __name__ == '__main__':
    convert()
