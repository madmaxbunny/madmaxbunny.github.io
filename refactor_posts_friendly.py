import os
import re
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, '_posts')

EMOJIS = ["💡", "🚀", "📄", "📌", "⚙️", "🟢", "🔑", "🔍", "🛠️", "📑", "⚡️", "✨", "📝", "📢", "👉", "😊", "🎉", "📂", "📊", "🌐", "⏱️", "📑"]

def remove_emojis(text):
    for em in EMOJIS:
        text = text.replace(em, "")
    # Also strip high unicode emojis
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', '', text)
    return text

def convert_to_friendly_tone(text):
    # Standardize headers to clean text without symbols
    text = re.sub(r'#+\s*(\d+\.\s*)?TL;DR.*', '## 요약', text, flags=re.IGNORECASE)
    text = re.sub(r'#+\s*(\d+\.\s*)?개요.*', '## 개요 및 배경', text)
    text = re.sub(r'#+\s*(\d+\.\s*)?핵심.*', '## 핵심 설명 및 코드', text)
    text = re.sub(r'#+\s*(\d+\.\s*)?요약.*', '## 정리하며', text)

    # Conversational sentence endings
    text = text.replace('입니다.', '이에요.')
    text = text.replace('합니다.', '해요.')
    text = text.replace('하십시요.', '해보세요.')
    text = text.replace('하십시오.', '해보세요.')
    text = text.replace('확인합니다.', '확인해보세요.')
    text = text.replace('사용됩니다.', '사용돼요.')
    text = text.replace('설정합니다.', '설정해볼게요.')
    text = text.replace('진행합니다.', '진행해보겠습니다.')

    # Clean double blockquotes / callouts
    text = re.sub(r'>\s*TL;DR.*', '', text)
    text = re.sub(r'>\s*💡.*', '', text)
    
    return text

def process_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        return

    frontmatter_raw = parts[1]
    body = parts[2].strip()

    try:
        meta = yaml.safe_load(frontmatter_raw)
    except Exception:
        meta = {}

    title = meta.get('title', 'Post')
    title_clean = remove_emojis(title).strip()
    meta['title'] = title_clean

    # Clean body
    body_clean = remove_emojis(body)
    body_friendly = convert_to_friendly_tone(body_clean)

    # Rebuild Markdown cleanly without emojis or extra decorative characters
    new_body = f"""
{title_clean}에 대한 정리 노트이에요. 참고하시는 데 도움되었으면 해요.

---

## 개요 및 배경

{title_clean}에 관해 실무와 개발 과정에서 알게 된 핵심 내용들을 공유해요.

---

## 핵심 설명 및 코드

{body_friendly}

---

## 정리하며

관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요.
"""

    # Fix Liquid tags if present
    if '{{' in new_body or '{%' in new_body:
        if '{% raw %}' not in new_body:
            new_body = "{% raw %}\n" + new_body.strip() + "\n{% endraw %}"

    # Clean multiple blank lines
    new_body = re.sub(r'\n{3,}', '\n\n', new_body)

    # Re-dump YAML frontmatter cleanly
    new_fm = yaml.dump(meta, allow_unicode=True, sort_keys=False).strip()
    new_file_content = f"---\n{new_fm}\n---\n{new_body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_file_content)
    print(f"Revamped: {filename}")

def main():
    print("Revamping all blog posts into friendly conversational tone without emojis...")
    for f in sorted(os.listdir(POSTS_DIR)):
        if f.endswith('.md'):
            process_file(os.path.join(POSTS_DIR, f))
    print("Completed friendly tone conversion successfully!")

if __name__ == '__main__':
    main()
