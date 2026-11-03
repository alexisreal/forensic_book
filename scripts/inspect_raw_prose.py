import subprocess
import re

def inspect_chapter_prose(ch_name):
    content = subprocess.check_output(["git", "show", f"426b946:chapters/{ch_name}"]).decode("utf-8")
    parts = re.split(r"\\begin\{lstlisting\}(?:\[.*?\])?.*?\\end\{lstlisting\}", content, flags=re.DOTALL)
    print(f"\n==================== {ch_name} ====================")
    p_num = 1
    for p in parts:
        for chunk in p.split("\n\n"):
            c = chunk.strip()
            lines = [l for l in c.splitlines() if l.strip() and not l.strip().startswith(("\\chapter", "\\section", "\\subsection", "\\subsubsection", "\\begin", "\\end", "\\vspace", "\\hrulefill"))]
            if lines and sum(len(l.split()) for l in lines) >= 8:
                text_block = " ".join(lines)
                print(f"[P{p_num:02d}] {text_block[:140]}...")
                p_num += 1

inspect_chapter_prose("cap03_deteccion_en_vivo.tex")
inspect_chapter_prose("cap05_monitoreo_usuarios.tex")
inspect_chapter_prose("cap14_veredicto_y_atribucion.tex")
