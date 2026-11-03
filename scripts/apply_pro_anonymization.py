#!/usr/bin/env python3
"""
apply_pro_anonymization.py
Implements professional anonymization across all TeX files in reporte-forense.
Conventions:
- RFC 5737: 192.0.2.0/24 (TEST-NET-1) for institutional subnet
- Domain: ifm.lab.edu.mx (Institute of Physics & Mathematics)
- Hostnames (Option A):
    * victima1 -> helios (primary server, 192.0.2.10)
    * victima2 -> atlas  (secondary server, 192.0.2.20)
    * victima3 -> io     (mail server, 192.0.2.25)
- Terminals: 192.0.2.29, 192.0.2.30, 192.0.2.67, 192.0.2.89 (admin), 192.0.2.250 (backup)
- Usernames:
    * xxxxxx (student) -> alopez
    * yyyyy (compromised webmail user) -> mherrera
    * weak password accounts -> cgarcia, alopez, jvaldez
    * sniffer captured passwords -> ********
"""

import os
import re
import glob

def process_content(text, filename=""):
    # 1. Domain and FQDN substitutions
    text = text.replace("ifm1.foo.bar.mx", "helios.ifm.lab.edu.mx")
    text = text.replace("victima1.foo.bar.mx", "helios.ifm.lab.edu.mx")
    text = text.replace("victima2.foo.bar.mx", "atlas.ifm.lab.edu.mx")
    text = text.replace("victima3.foo.bar.mx", "io.ifm.lab.edu.mx")
    text = text.replace("foo.bar.mx", "ifm.lab.edu.mx")
    text = text.replace("victima1.com", "helios.ifm.lab.edu.mx")

    # 2. IP Addresses (longer/more specific first)
    text = text.replace("xxx.xxx.xxx.29", "192.0.2.29")
    text = text.replace("xxx.xxx.xxx.30", "192.0.2.30")
    text = text.replace("xxx.xxx.xxx.67", "192.0.2.67")
    text = text.replace("xxx.xxx.xxx.89", "192.0.2.89")
    text = re.sub(r'xxx\.xxx\.xxx\.2\b', '192.0.2.20', text)
    text = text.replace("xxx.xxx.xxx.xxx", "192.0.2.250")

    # 3. Disk images and specific file prefixes
    text = text.replace("victima1-master-dd.img", "helios-master-dd.img")
    text = text.replace("victima1-rh", "helios-rh")
    text = text.replace("victima1-root.img-dead-307489", "helios-root.img-dead-307489")
    text = text.replace("victima1-root.img-dead-307490", "helios-root.img-dead-307490")
    text = text.replace("victima2`.seen", "atlas`.seen")

    # 4. Cap 04 sniffer passwords and SSH student account
    text = re.sub(r'Password:\s+x{4,}', 'Password: ********', text)
    text = re.sub(r"xxxxxx@victima2's password:\s+x{4,}", "alopez@atlas's password: ********", text)
    text = text.replace("ssh -l xxxxxx victima2", "ssh -l alopez atlas")
    text = text.replace("/home/est/xxxxxx/", "/home/est/alopez/")

    # 5. Cap 13 user yyyyy
    text = text.replace("Accepted password for yyyyy", "Accepted password for mherrera")
    text = text.replace("BAD SU yyyyy to root", "BAD SU mherrera to root")
    text = text.replace("cuenta yyyyy por", "cuenta \\texttt{mherrera} por")

    # 6. Cap 14 weak password accounts
    text = text.replace(
        r"\texttt{xxxxx}, \texttt{xxxxxx} y \texttt{xxxxxxxx}",
        r"\texttt{cgarcia}, \texttt{alopez} y \texttt{jvaldez}"
    )

    # 7. Hostname word substitutions
    # We do word-boundary replacements for victima1, victima2, victima3
    text = re.sub(r'\bvictima1\b', 'helios', text)
    text = re.sub(r'\bvictima2\b', 'atlas', text)
    text = re.sub(r'\bvictima3\b', 'io', text)

    return text

def main():
    files = sorted(
        glob.glob("chapters/*.tex") +
        glob.glob("appendices/*.tex") +
        glob.glob("frontmatter/*.tex") +
        ["main.tex"]
    )

    total_changes = 0
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            orig = fp.read()
        processed = process_content(orig, f)
        if orig != processed:
            diff_lines = len([l for l in processed.splitlines() if l not in orig.splitlines()])
            print(f"Modifying {f} (~{diff_lines} lines changed)")
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(processed)
            total_changes += 1

    print(f"\nDone. Successfully updated {total_changes} files.")

if __name__ == "__main__":
    main()
