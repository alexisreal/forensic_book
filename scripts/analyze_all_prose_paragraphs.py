import subprocess
import re

chapters = [
    "cap01_entorno_tecnologico.tex",
    "cap02_metodologia_forense.tex",
    "cap03_deteccion_en_vivo.tex",
    "cap04_siembra_servicios_malware.tex",
    "cap05_monitoreo_usuarios.tex",
    "cap06_analisis_referencia_rpm.tex",
    "cap07_antivirus_rootkits.tex",
    "cap08_lineas_tiempo_mactime.tex",
    "cap09_mineria_bitacoras.tex",
    "cap10_cuentas_comprometidas.tex",
    "cap11_recuperacion_archivos_borrados.tex",
    "cap12_correlacion_multisistema.tex",
    "cap13_servidor_correo_webmail.tex",
    "cap14_veredicto_y_atribucion.tex",
    "cap15_retrospectiva_20_anios.tex",
]

total_paras = 0
for ch in chapters:
    try:
        content = subprocess.check_output(["git", "show", f"426b946:chapters/{ch}"]).decode("utf-8")
    except Exception as e:
        print(f"Error loading {ch}: {e}")
        continue
    
    # split by listings
    parts = re.split(r"\\begin\{lstlisting\}(?:\[.*?\])?.*?\\end\{lstlisting\}", content, flags=re.DOTALL)
    paras = []
    for p in parts:
        for chunk in p.split("\n\n"):
            c = chunk.strip()
            # filter out pure macro lines or short headers
            lines = [l for l in c.splitlines() if l.strip() and not l.strip().startswith(("\\chapter", "\\section", "\\subsection", "\\subsubsection", "\\begin", "\\end", "\\vspace", "\\hrulefill"))]
            if lines and sum(len(l.split()) for l in lines) >= 8:
                paras.append("\n".join(lines))
    print(f"{ch}: {len(paras)} prose paragraphs")
    total_paras += len(paras)

print(f"\nTotal prose paragraphs to review across the full book: {total_paras}")
