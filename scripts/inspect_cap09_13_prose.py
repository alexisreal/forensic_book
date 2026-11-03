import os
import re

chapters = [
    "cap09_mineria_bitacoras.tex",
    "cap10_cuentas_comprometidas.tex",
    "cap12_correlacion_multisistema.tex",
    "cap13_servidor_correo_webmail.tex",
]

for ch in chapters:
    path = os.path.join("/Users/alexis/work/reporte-forense/chapters", ch)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    parts = re.split(r"\\begin\{lstlisting\}(?:\[.*?\])?.*?\\end\{lstlisting\}", content, flags=re.DOTALL)
    print(f"\n==================== {ch} ====================")
    for p in parts:
        for chunk in p.split("\n\n"):
            c = chunk.strip()
            lines = [l for l in c.splitlines() if l.strip() and not l.strip().startswith(("\\chapter", "\\section", "\\subsection", "\\subsubsection", "\\begin", "\\end", "\\vspace", "\\hrulefill"))]
            if lines and sum(len(l.split()) for l in lines) >= 6:
                text_block = " ".join(lines)
                print(f"-> {text_block[:130]}...")
