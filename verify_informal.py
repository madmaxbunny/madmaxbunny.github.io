import os
import re

POSTS_DIR = '_posts'
informal_terms = ['해요', '이에요', '예요', '해볼게요', '해보세요', '해봐요', '주세요', '있어요', '없어요', '됐어요', '되었어요', '했어요']

found = 0
for f in sorted(os.listdir(POSTS_DIR)):
    if not f.endswith('.md'):
        continue
    filepath = os.path.join(POSTS_DIR, f)
    with open(filepath, 'r', encoding='utf-8') as fp:
        content = fp.read()

    lines = content.split('\n')
    in_cb = False
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            in_cb = not in_cb
            continue
        if in_cb:
            continue
        for term in informal_terms:
            if term in line:
                print(f'{f}:{idx} [{term}] -> {line.strip()}')
                found += 1

print(f"Total remaining informal terms outside codeblocks: {found}")
