import re

with open("/Users/alexis/work/reporte-forense/original/reporte-publico-original.tex", "r", encoding="latin1") as f:
    lines = f.readlines()

headings = []
for idx, line in enumerate(lines):
    l_strip = line.strip()
    if l_strip.startswith(("\\section", "\\subsection", "\\subsubsection")):
        headings.append((idx, l_strip))

for i, (line_no, heading) in enumerate(headings):
    next_line = headings[i+1][0] if i+1 < len(headings) else len(lines)
    length = next_line - line_no
    print(f"L{line_no+1:4d} - L{next_line:4d} ({length:4d} lines): {heading}")
