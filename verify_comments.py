import os

POSTS_DIR = '_posts'
comment_lines = []

for f in sorted(os.listdir(POSTS_DIR)):
    if not f.endswith('.md'):
        continue
    filepath = os.path.join(POSTS_DIR, f)
    with open(filepath, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()

    in_cb = False
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            in_cb = not in_cb
            continue
        if in_cb:
            continue
        if '댓글' in line:
            comment_lines.append((f, idx, line.strip()))

print(f"Total remaining mentions of 댓글: {len(comment_lines)}")
for cl in comment_lines:
    print(f"{cl[0]}:{cl[1]} -> {cl[2]}")
