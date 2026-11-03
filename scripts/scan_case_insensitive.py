import glob
import re
import os

ACCENT_PAIRS = [
    # (wrong, right)
    ("revisara", "revisará"),
    ("estudiaran", "estudiarán"),
    ("mostraran", "mostrarán"),
    ("explicara", "explicará"),
    ("encontraran", "encontrarán"),
    ("incluiran", "incluirán"),
    ("recuperara", "recuperará"),
    ("trabajo", "trabajó"), # wait: "el trabajo" vs "se trabajó"
    ("realizo", "realizó"),
    ("analizo", "analizó"),
    ("encontro", "encontró"),
    ("procedio", "procedió"),
    ("recupero", "recuperó"),
    ("detecto", "detectó"),
    ("observo", "observó"),
    ("confirmo", "confirmó"),
    ("verifico", "verificó"),
    ("ejecuto", "ejecutó"),
    ("instalo", "instaló"),
    ("descubrio", "descubrió"),
    ("inicio", "inició"),
    ("trato", "trató"),
    ("borro", "borró"),
    ("creo", "creó"),
    ("tambien", "también"),
    ("ademas", "además"),
    ("despues", "después"),
    ("ningun", "ningún"),
    ("segun", "según"),
    ("linea", "línea"),
    ("lineas", "líneas"),
    ("maquina", "máquina"),
    ("maquinas", "máquinas"),
    ("bitacora", "bitácora"),
    ("bitacoras", "bitácoras"),
    ("codigo", "código"),
    ("codigos", "códigos"),
    ("numero", "número"),
    ("numeros", "números"),
    ("periodo", "período"),
    ("ultimo", "último"),
    ("ultima", "última"),
    ("ultimos", "últimos"),
    ("ultimas", "últimas"),
    ("proposito", "propósito"),
    ("propositos", "propósitos"),
    ("metodo", "método"),
    ("metodos", "métodos"),
    ("tactica", "táctica"),
    ("tacticas", "tácticas"),
    ("tecnica", "técnica"),
    ("tecnicas", "técnicas"),
    ("arbol", "árbol"),
    ("arboles", "árboles"),
    ("exito", "éxito"),
    ("comun", "común"),
    ("comunes", "comunes"),
    ("unicamente", "únicamente"),
    ("unico", "único"),
    ("unica", "única"),
    ("unicos", "únicos"),
    ("unicas", "únicas"),
    ("accesaba", "accedía"),
    ("accesaban", "accedían"),
    ("accesar", "acceder"),
    ("accesó", "accedió"),
    ("accesaron", "accedieron"),
    ("checar", "verificar"),
    ("checo", "verificó"),
    ("checó", "verificó"),
    ("checaron", "verificaron"),
    ("chequeo", "verificación"),
    ("password", "contraseña"),
    ("passwords", "contraseñas"),
]

ch_dir = "/Users/alexis/work/reporte-forense/chapters"
files = sorted(glob.glob(os.path.join(ch_dir, "*.tex")))

found_total = 0
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    parts = re.split(r"\\begin\{lstlisting\}(?:\[.*?\])?.*?\\end\{lstlisting\}", content, flags=re.DOTALL)
    prose = " ".join(parts)
    
    file_hits = []
    for wrong, right in ACCENT_PAIRS:
        # if verb with ambiguous noun like "trabajo", check "se trabajo" or context
        if wrong == "trabajo":
            m = re.findall(r"\b(se\s+trabajo)\b", prose, re.IGNORECASE)
        elif wrong == "trato":
            m = re.findall(r"\b(se\s+trato)\b", prose, re.IGNORECASE)
        elif wrong == "inicio":
            m = re.findall(r"\b(se\s+inicio)\b", prose, re.IGNORECASE)
        else:
            m = re.findall(r"\b(" + wrong + r")\b", prose, re.IGNORECASE)
        if m:
            file_hits.append((wrong, len(m)))
            found_total += len(m)
    if file_hits:
        print(f"{os.path.basename(f)}: {file_hits}")

print(f"\nTotal potential missing accents/corrections found: {found_total}")
