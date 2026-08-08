import os
import re

POSTS_DIR = '_posts'

def clean_post(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove unneeded empty lines with spaces
    content = re.sub(r'^[ \t]+$', '', content, flags=re.MULTILINE)
    
    # Remove leading spaces before ``` fence markers
    content = re.sub(r'^[ \t]+```', '```', content, flags=re.MULTILINE)

    # Clean double {% raw %} tags if any
    content = re.sub(r'({% raw %}\s*)+', '{% raw %}\n', content)
    content = re.sub(r'(\s*{% endraw %})+', '\n{% endraw %}', content)

    # Ensure clean codeblock formatting
    lines = content.split('\n')
    cleaned = []
    in_cb = False

    for line in lines:
        if line.startswith('```'):
            in_cb = not in_cb
            cleaned.append(line.strip())
        elif in_cb:
            # strip up to 4 leading spaces inside codeblock
            if line.startswith('    '):
                cleaned.append(line[4:])
            elif line.startswith('\t'):
                cleaned.append(line[1:])
            else:
                cleaned.append(line)
        else:
            cleaned.append(line)

    final_content = '\n'.join(cleaned)
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)

    if final_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        return True
    return False

def main():
    fixed = 0
    for f in os.listdir(POSTS_DIR):
        if f.endswith('.md'):
            if clean_post(os.path.join(POSTS_DIR, f)):
                fixed += 1
    print(f"Cleaned formatting in {fixed} post files!")

if __name__ == '__main__':
    main()
