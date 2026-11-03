import glob
import re
import os

patterns = [
    (r"\b(se revisara|se estudiaran|se encontro|se procedio|se realizo|se analizo|se trabajo|se recupero)\b", "Verbos sin tilde"),
    (r"\\verb\+[^+]+\+", "Comandos \\verb residuales"),
    (r"\b(estara|haran|sera|seran|estan|ningun|ademas|tambien|despues)\b", "Palabras sin tilde"),
    (r"[-—_]{10,}", "Líneas de guiones residuales"),
    (r"\\\\", "Saltos manuales \\\\ innecesarios"),
]

for p in sorted(glob.glob("/Users/alexis/work/reporte-forense/chapters/*.tex")):
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    issues = []
    for pat, label in patterns:
        m = re.findall(pat, text, re.IGNORECASE)
        if m:
            issues.append(f"{label}: {len(m)}")
    if issues:
        fname = os.path.basename(p)
        print(f"{fname}: {'; '.join(issues)}")
