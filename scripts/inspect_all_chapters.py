import glob
import re
import os

ch_files = sorted(glob.glob("/Users/alexis/work/reporte-forense/chapters/*.tex"))

print(f"Inspecting {len(ch_files)} chapters for editorial structure...")

for fpath in ch_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    
    sections = re.findall(r"\\(section|subsection|subsubsection)\*?\{([^}]+)\}", text)
    listings = len(re.findall(r"\\begin\{lstlisting\}", text))
    alltt = len(re.findall(r"\\begin\{alltt\}", text))
    verb = len(re.findall(r"\\verb\+", text))
    dashes = len(re.findall(r"[-—_]{5,}", text))
    
    sec_names = [s[1] for s in sections]
    print(f"\n[{fname}] Lines: {len(text.splitlines())} | Sections: {len(sections)} | Listings: {listings} | alltt: {alltt} | \\verb: {verb}")
    if sec_names:
        print("   Sections:", " -> ".join(sec_names[:4]))
