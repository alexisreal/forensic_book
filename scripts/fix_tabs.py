#!/usr/bin/env python3
import glob

for f in sorted(glob.glob('chapters/*.tex') + glob.glob('frontmatter/*.tex') + glob.glob('appendices/*.tex')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if '\t' in c:
        # replace tab followed by ext with \text
        c = c.replace('\text', '\\text')
        # replace any remaining tab with 4 spaces if in listing, or backslash if before a letter
        c = c.replace('\t', '    ')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

print("Done fixing tabs.")
