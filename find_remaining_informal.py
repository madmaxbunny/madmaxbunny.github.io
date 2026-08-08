import os
import re

POSTS_DIR = '_posts'

informal_patterns = [
    (r'이에요', '입니다'),
    (r'예요', '입니다'),
    (r'공유해요', '공유합니다'),
    (r'공유해볼게요', '공유하고자 합니다'),
    (r'정리해봤어요', '정리했습니다'),
    (r'정리해볼게요', '정리하고자 합니다'),
    (r'해볼게요', '해보겠습니다'),
    (r'해보세요', '해보시기 바랍니다'),
    (r'해봐요', '해보시기 바랍니다'),
    (r'주세요', '주시기 바랍니다'),
    (r'있어요', '있습니다'),
    (r'없어요', '없습니다'),
    (r'되었어요', '되었습니다'),
    (r'됐어요', '되었습니다'),
    (r'했어요', '했습니다'),
    (r'좋겠어요', '바랍니다'),
]

def scan_and_fix():
    fixed_files = 0
    total_replacements = 0

    for f in os.listdir(POSTS_DIR):
        if not f.endswith('.md'):
            continue
        filepath = os.path.join(POSTS_DIR, f)
        with open(filepath, 'r', encoding='utf-8') as fp:
            content = fp.read()

        lines = content.split('\n')
        new_lines = []
        in_cb = False
        file_changed = False

        for line in lines:
            if line.strip().startswith('```'):
                in_cb = not in_cb
                new_lines.append(line)
                continue

            if in_cb:
                # Do not change inside code blocks
                new_lines.append(line)
                continue

            new_line = line
            for pat, rep in informal_patterns:
                if re.search(pat, new_line):
                    new_line = re.sub(pat, rep, new_line)
                    file_changed = True
                    total_replacements += 1

            new_lines.append(new_line)

        if file_changed:
            with open(filepath, 'w', encoding='utf-8') as fp:
                fp.write('\n'.join(new_lines))
            fixed_files += 1

    print(f"Scanned all posts: Fixed {total_replacements} informal phrases across {fixed_files} post files!")

if __name__ == '__main__':
    scan_and_fix()
