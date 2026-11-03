import glob
import re
import os

ISP_REPLACEMENTS = [
    # Prodigy and Telemedia hostnames
    (r"\bdup-200-64-(\d+)-(\d+)\.prodigy\.net\.mx\b", r"dialup-198-18-10-\2.isp-acceso.net"),
    (r"\bdsl-200-78-118-(\d+)\.prodigy\.net\.mx\b", r"dsl-198-51-100-\1.isp-acceso.net"),
    (r"\bdsl-200-67-75-(\d+)\.prodigy\.net\.mx\b", r"dsl-203-0-113-\1.isp-acceso.net"),
    (r"\bdsl-200-67-(\d+)-(\d+)\.prodigy\.net\.mx\b", r"dsl-203-0-\1-\2.isp-acceso.net"),
    (r"\bdup-200-(\d+)-(\d+)-(\d+)\.prodigy\.net\.mx\b", r"dialup-198-18-\2-\3.isp-acceso.net"),
    (r"\bdsl-200-(\d+)-(\d+)-(\d+)\.prodigy\.net\.mx\b", r"dsl-198-18-\2-\3.isp-acceso.net"),
    (r"\bhost-200\.77\.149\.(\d+)-cust\.telemedia\.net\.mx\b", r"host-192-0-2-\1.red-telecom.net"),
    (r"\bhost-200\.77\.(\d+)\.(\d+)-cust\.telemedia\.net\.mx\b", r"host-198-18-\1-\2.red-telecom.net"),
    (r"\b[a-zA-Z0-9.-]+\.telemedia\.net\.mx\b", r"nodo-acceso.red-telecom.net"),
    (r"\bterra\.com\.ar\b", r"correo-remoto.net"),
    (r"\bterra\.com\b", r"correo-externo.net"),
    (r"\bka0sphere\.[a-zA-Z0-9.-]+\b", r"botnet-c2.dns-dinamico.org"),
    (r"\bcha0sphere\.[a-zA-Z0-9.-]+\b", r"botnet-c2.dns-dinamico.org"),
    (r"\bhinet\.net\b", r"isp-internacional.net"),
]

for f in sorted(glob.glob("/Users/alexis/work/reporte-forense/**/*.tex", recursive=True)):
    if "original" in f: continue
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    orig = content
    for pat, rep in ISP_REPLACEMENTS:
        content = re.sub(pat, rep, content, flags=re.IGNORECASE)
    if content != orig:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(content)
        print(f"Anonymized ISP hostnames in: {os.path.basename(f)}")
