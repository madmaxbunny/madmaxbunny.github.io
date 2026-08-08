import os
import re
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, '_posts')

EMOJIS = ["💡", "🚀", "📄", "📌", "⚙️", "🟢", "🔑", "🔍", "🛠️", "📑", "⚡️", "✨", "📝", "📢", "👉", "😊", "🎉", "📂", "📊", "🌐", "⏱️", "📑"]

def remove_emojis(text):
    for em in EMOJIS:
        text = text.replace(em, "")
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', '', text)
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

    # Remove repeated robotic intro lines if present
    body_clean = re.sub(r'^[^\n]*에 대한 정리 노트이에요[^\n]*\n*', '', body_clean, flags=re.MULTILINE)
    body_clean = re.sub(r'^[^\n]*관해 실무와 개발 과정에서 알게 된 핵심 내용들을 공유해요[^\n]*\n*', '', body_clean, flags=re.MULTILINE)

    # Standardize section headers cleanly
    body_clean = re.sub(r'#+\s*(\d+\.\s*)?개요.*', '## 1. 개요 및 배경', body_clean)
    body_clean = re.sub(r'#+\s*(\d+\.\s*)?핵심.*', '## 2. 핵심 설명 및 설정 가이드', body_clean)
    body_clean = re.sub(r'#+\s*(\d+\.\s*)?정리.*', '## 3. 정리하며', body_clean)

    # Clean double raw blocks
    body_clean = re.sub(r'({% raw %}\s*)+', '{% raw %}\n', body_clean)
    body_clean = re.sub(r'(\s*{% endraw %})+', '\n{% endraw %}', body_clean)

    # Rebuild Markdown with Clean Summary Box and Natural Conversational Tone
    new_body = f"""
> **[핵심 요약]**
> {title_clean} 작업에 대해 실무에서 검증된 핵심 설정 및 처리 방법을 정돈해둔 노트이에요.

---

## 1. 개요 및 배경

{title_clean}에 관해 개발 및 인프라 운용 과정에서 접했던 내용들을 공유해볼게요.

---

## 2. 핵심 설명 및 설정 가이드

{body_clean.strip()}

---

## 3. 정리하며

관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있으시다면 언제든 댓글로 편하게 말씀해주세요.
"""

    # Liquid escaping check
    if '{{' in new_body or '{%' in new_body:
        if '{% raw %}' not in new_body:
            new_body = "{% raw %}\n" + new_body.strip() + "\n{% endraw %}"

    new_body = re.sub(r'\n{3,}', '\n\n', new_body)

    new_fm = yaml.dump(meta, allow_unicode=True, sort_keys=False).strip()
    new_file_content = f"---\n{new_fm}\n---\n{new_body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_file_content)
    print(f"Refactored: {filename}")

def main():
    print("Refactoring all posts with clean TL;DR summary box and natural conversational tone...")
    for f in sorted(os.listdir(POSTS_DIR)):
        if f.endswith('.md'):
            process_file(os.path.join(POSTS_DIR, f))
    print("Completed natural conversational tone refactoring successfully!")

if __name__ == '__main__':
    main()
