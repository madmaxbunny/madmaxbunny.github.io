import os
import re

POSTS_DIR = '_posts'

def remove_comment_mentions(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match comment closing lines
    patterns = [
        r'관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있다면 댓글로 편하게 남겨주시기 바랍니다\.\n*',
        r'관련해서 궁금하신 점이나 나눠보고 싶은 의견이 있으시다면 언제든 댓글로 편하게 말씀해주세요\.\n*',
        r'관련 내용에 대해 궁금한 점이 있으시다면 언제든 편하게 질문해주세요\.\n*',
        r'추가 문의나 개선사항은 포스트 하단 댓글 또는 GitHub 이슈로 전달해 주세요\.\n*',
        r'댓글로 편하게[^\n]*\n*',
        r'댓글로[^\n]*\n*'
    ]

    new_content = content
    for pat in patterns:
        new_content = re.sub(pat, '', new_content)

    # Clean double blank lines at the end of section 3
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    cleaned_count = 0
    for f in sorted(os.listdir(POSTS_DIR)):
        if f.endswith('.md'):
            if remove_comment_mentions(os.path.join(POSTS_DIR, f)):
                cleaned_count += 1
    print(f"Successfully removed comment closing lines across {cleaned_count} post files!")

if __name__ == '__main__':
    main()
