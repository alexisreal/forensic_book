#!/usr/bin/env python3
import glob
import re

files = sorted(glob.glob("chapters/*.tex") + glob.glob("frontmatter/*.tex") + glob.glob("appendices/*.tex"))

def fix_content(text):
    # Regex to find \texttt{...} and replace unescaped _ with \_ inside it
    def repl_tt(m):
        inner = m.group(1)
        fixed_inner = re.sub(r'(?<!\\)_', r'\_', inner)
        return r'\texttt{' + fixed_inner + '}'
    
    # Process \texttt{...} (handling non-nested)
    # Also handle \textit{...} and \textbf{...}
    for macro in ['texttt', 'textit', 'textbf']:
        pattern = r'\\' + macro + r'\{([^{}]+)\}'
        # run multiple times to catch any
        for _ in range(3):
            text = re.sub(pattern, lambda m: r'\\' + macro + '{' + re.sub(r'(?<!\\)_', r'\_', m.group(1)) + '}', text)
    
    return text

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        orig = fp.read()
    fixed = fix_content(orig)
    if orig != fixed:
        print(f"Fixing underscores in {f}")
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(fixed)

print("Done fixing underscores.")
