import glob
import re
import os

ch_dir = "/Users/alexis/work/reporte-forense/chapters"
files = sorted(glob.glob(os.path.join(ch_dir, "*.tex")))

print("=== DEEP AUDIT OF ALL CHAPTERS ===")
total_issues = 0

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    fname = os.path.basename(f)
    
    # 1. Check for \verb
    verbs = re.findall(r"\\verb\+[^+]+\+", content)
    
    # 2. Check for verbatim / alltt
    verbatims = re.findall(r"\\begin\{(?:verbatim|alltt)\}", content)
    
    # 3. Check for double formatting like \textit{\textit{...}} or \textbf{\textbf{...}}
    double_fmt = re.findall(r"\\(?:textbf|textit|emph)\{\\(?:textbf|textit|emph)\{[^}]+\}\}", content)
    
    # 4. Check for dash lines outside lstlisting
    parts = re.split(r"\\begin\{lstlisting\}(?:\[.*?\])?.*?\\end\{lstlisting\}", content, flags=re.DOTALL)
    dashes_outside = []
    for p in parts:
        dashes_outside.extend(re.findall(r"[-—_]{8,}", p))
        
    # 5. Check for unaccented words outside lstlisting
    prose = " ".join(parts)
    unaccented = []
    bad_words = [
        "se revisara", "se estudiaran", "se encontro", "se procedio", "se realizo", "se analizo", 
        "se trabajo", "se recupero", "se observo", "se verifico", "se detecto", "se ejecuto",
        "accesaba", "accesó", "checar", "checó", "password", "passwords", "tambien", "ademas", 
        "despues", "ningun", "comun", "arbol", "codigo", "bitacora", "maquina", 
        "linea", "lineas", "ultimo", "ultima", "proposito", "metodo"
    ]
    for bw in bad_words:
        if bw in ["password", "passwords"]:
            matches = [m for m in re.findall(r"(?<!shadow\s)\b" + bw + r"\b", prose, re.IGNORECASE)]
        else:
            matches = re.findall(r"\b" + bw + r"\b", prose, re.IGNORECASE)
        if matches:
            unaccented.append((bw, len(matches)))
            
    # 6. Check for \section* or \subsection*
    starred_headings = re.findall(r"\\(?:part|chapter|section|subsection|subsubsection)\*\{[^}]+\}", content)
    
    issues = []
    if verbs: issues.append(f"\\verb: {len(verbs)}")
    if verbatims: issues.append(f"verbatim/alltt: {len(verbatims)}")
    if double_fmt: issues.append(f"double_fmt: {len(double_fmt)} ({double_fmt[:2]})")
    if dashes_outside: issues.append(f"dashes_outside: {len(dashes_outside)}")
    if starred_headings: issues.append(f"starred_headings: {len(starred_headings)} ({starred_headings})")
    if unaccented: issues.append(f"unaccented: {unaccented}")
    
    if issues:
        total_issues += len(issues)
        issues_str = "; ".join(issues)
        print(f"FAILED: {fname} -> {issues_str}")
    else:
        print(f"PASSED: {fname}")

print(f"\nTotal problem categories detected: {total_issues}")
