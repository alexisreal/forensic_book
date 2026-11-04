# Linux Forensics: A Real Case

**Autopsy of a Cyberattack on Live Production Servers (2005 – 2025)**  
*Incident Response, Volatile Memory, and Multi-System Event Correlation*

**English** | [Versión en Español](README_es.md)

* **Author:** Alexis Real Santillán
* **Professional Profile:** Cybersecurity, Cloud Architecture, and Critical Infrastructure Consultant | CTO at [Linux Open Source de México](https://linuxopensource.org)
* **Portfolio & Curriculum Vitae:** [alexisreal.github.io/cv](https://alexisreal.github.io/cv/)
* **Contact:** [alexisreal@gmail.com](mailto:alexisreal@gmail.com)
* **Institutional Context:** Based on the forensic investigation directed by the author during his tenure as Computer Systems Administrator at the Institute of Physics and Mathematics (IFM), Universidad Michoacana de San Nicolás de Hidalgo (UMSNH).
* **Publication License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) (Open digital edition, published without commercial ISBN).

---

## Direct PDF Downloads

* 📕 **[English Edition PDF (main_en.pdf)](main_en.pdf)** — 173 pages, complete English translation, translated TikZ diagrams, full logs, and coordinated back cover.
* 📘 **[Spanish Edition PDF (main.pdf)](main.pdf)** — 181 pages, original Spanish text, complete technical apparatus, and forensic study guide.

---

## Pedagogical & Technical Scope

This book is structured as a **training manual and real-world reference case study for Digital Forensics and Incident Response (DFIR)** professionals, security analysts, and university students. It combines the technical rigor, original raw artifacts, and physical evidentiary findings of a live server compromise with a pedagogical apparatus aligned with international standards:

* **ISO/IEC 27037:2012:** Guidelines for identification, collection, acquisition, and preservation of digital evidence.
* **NIST SP 800-86:** Guide to Integrating Forensic Techniques into Incident Response.
* **RFC 5737 & RFC 2606:** Standardized documentation IP address spaces (`192.0.2.0/24`) and hostname anonymization preserving forensic subnet relationships.

---

## Repository Structure

The repository maintains two parallel, fully consistent editions:

```
forensic_book/
├── main.tex                            # Master LaTeX document (Spanish Edition)
├── main_en.tex                         # Master LaTeX document (English Edition)
├── main.pdf                            # Compiled Spanish book (181 pages)
├── main_en.pdf                         # Compiled English book (173 pages)
├── README.md                           # English documentation (this file)
├── README_es.md                        # Documentación en español
│
├── config/
│   ├── preamble.tex                    # Typography, geometry & Spanish callouts
│   └── preamble_en.tex                 # Typography, geometry & English callouts
│
├── frontmatter/ & frontmatter_en/
│   ├── portada.tex                     # Classic typographic cover (Bloodhound engraving)
│   ├── contraportada.tex               # Coordinated back cover with synopsis and author bio
│   ├── creditos.tex                    # Legal notice, CC BY-SA 4.0, and Gemini credits
│   ├── dedicatoria.tex                 # Dedication
│   ├── prefacio.tex                    # Preface: 20 years of Unix forensic evolution
│   ├── resumen.tex                     # Forensic executive summary
│   └── guia_estudio.tex                # Methodological guide, axioms & NIST/ISO matrix
│
├── chapters/ & chapters_en/
│   ├── cap01_entorno_tecnologico.tex   # Hardware topology, server specs, TikZ diagram
│   ├── cap02_metodologia_forense.tex   # Chain of custody, acquisition, and live triage
│   ├── cap03_deteccion_en_vivo.tex     # SUID/SGID binaries and suspicious processes
│   ├── cap04_siembra_servicios_malware.tex # IRC bots, dsniff sniffer, and credential harvesting
│   ├── cap05_monitoreo_usuarios.tex    # Active surveillance, Process Accounting (acct), tty logs
│   ├── cap06_analisis_referencia_rpm.tex # RPM database verification & Suckit v1.3b rootkit
│   ├── cap07_antivirus_rootkits.tex    # Unix/RST.A ELF infector and Ext2 immutable bits (+i/+a)
│   ├── cap08_lineas_tiempo_mactime.tex # TCT mactime timelines and hour-zero reconstruction
│   ├── cap09_mineria_bitacoras.tex     # Log correlation (auth.log, daemon.log, wtmp, xferlog)
│   ├── cap10_cuentas_comprometidas.tex # Compromised accounts, o0o.tar archive, and dump.sh
│   ├── cap11_recuperacion_archivos_borrados.tex # Orphan inodes, file carving, and the "algo" lead
│   ├── cap12_correlacion_multisistema.tex # Lateral movement and pivoting to secondary hosts
│   ├── cap13_servidor_correo_webmail.tex # Mail server intrusion, administrative abuse & webmail
│   ├── cap14_veredicto_y_atribucion.tex # Expert verdict: external adversary vs internal actor
│   └── cap15_retrospectiva_20_anios.tex # 20-year retrospective: RAM, eBPF, and Cloud DFIR
│
├── appendices/ & appendices_en/
│   ├── apendice_a_iocs.tex             # Catalog of Indicators of Compromise (IoCs)
│   ├── apendice_b_bitacoras_completas.tex # Annotated system logs and forensic audit trails
│   ├── apendice_c_glosario.tex         # Comprehensive 40+ term DFIR glossary
│   ├── apendice_d_comandos_forenses.tex # Command-line forensic cheat sheet
│   └── apendice_e_cadena_custodia_modelo.tex # ISO/IEC 27037 chain of custody template
│
├── biblio/
│   ├── bibliografia.tex                # Spanish bibliography
│   └── bibliografia_en.tex             # English bibliography
└── img/                                # Figures and illustrations (sabueso_color.jpg)
```

---

## Building from Source

The book compiles with modern TeX engines. We recommend **Tectonic** for its zero-configuration package management and reproducibility:

```bash
# Install Tectonic (macOS via Homebrew):
brew install tectonic

# Build the English edition:
tectonic main_en.tex

# Build the Spanish edition:
tectonic main.tex
```

Alternatively, you can compile using `pdflatex` or `xelatex`:

```bash
# Two passes are required to resolve cross-references and the table of contents:
pdflatex main_en.tex
pdflatex main_en.tex
```

---

## Key Features

* **Historical Perspective Boxes (`perspectiva20`):** Practical sidebars comparing 2004/2005 investigative techniques against modern tooling (EDR, Volatility 3, eBPF, and Zero Trust architectures).
* **Integrity Warnings (`advertencia`):** Detailed analysis of anti-forensics mechanisms encountered during the live investigation.
* **Forensic Challenges (`retoforense`):** Socratic questions and practical deductive exercises placed throughout chapters for classroom or self-study assessment.
* **Vector Diagrams:** High-resolution TikZ network topologies and attack timeline visualizations.
* **Authentic Audit Logs:** Complete, preserved terminal sessions, sniffer logs, process accounting records, and inode metadata.

---

## Editorial Credits & Technical Assistance

* **Original Work:** Written and conceived in Spanish by Alexis Real Santillán.
* **English Translation:** Translated into English with the assistance of Google Gemini.
* **Technical Illustrations & Typographical Design:** TikZ vector architecture diagrams, back cover design, and typographical style revisions across both editions were assisted by Google Gemini.

---

## License

This work is licensed under the **[Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)**. You are free to share, copy, distribute, and adapt the material for academic, commercial, or professional purposes provided that proper attribution is given to the author and derivative works are distributed under the same license.
