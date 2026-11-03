#!/usr/bin/env python3
import glob

for f in sorted(glob.glob('chapters/*.tex') + glob.glob('frontmatter/*.tex') + glob.glob('appendices/*.tex')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    orig = c
    c = c.replace(r'\\\textbf', r'\textbf')
    c = c.replace(r'\\\textit', r'\textit')
    c = c.replace(r'\\\texttt', r'\texttt')
    c = c.replace(r'\\textbf', r'\textbf')
    c = c.replace(r'\\textit', r'\textit')
    c = c.replace(r'\\texttt', r'\texttt')
    if c != orig:
        print(f"Fixed slashes in {f}")
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

print("Done fixing slashes.")
