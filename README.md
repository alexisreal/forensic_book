# Linux Forensics: A Real Case

**Autopsy of a Cyberattack on Live Production Servers (2005 – 2025)**  
*Incident Response, Volatile Memory, and Multi-System Event Correlation*

[![Curriculum Vitae](https://img.shields.io/badge/Curriculum%20Vitae-alexisreal.github.io%2Fcv-2ea44f?style=for-the-badge&logo=github)](https://alexisreal.github.io/cv/)
[![Linux Open Source de México](https://img.shields.io/badge/Linux%20Open%20Source%20de%20M%C3%A9xico-linuxopensource.org-0078d7?style=for-the-badge&logo=linux)](https://linuxopensource.org)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by-sa/4.0/)

> **Language navigation:** **English (Primary)** | [Saltar a la Versión en Español ↓](#versión-en-español-anatomía-forense-de-una-intrusión)

---

### Author & Technical Leadership

* **Author:** **Alexis Real Santillán**  
  *Consultant in Cybersecurity, Cloud Architecture, and Critical Infrastructure.*
* **Technical Leadership:** CTO at [**Linux Open Source de México**](https://linuxopensource.org) ([linuxopensource.org](https://linuxopensource.org))
* **Curriculum Vitae & Portfolio:** [**https://alexisreal.github.io/cv/**](https://alexisreal.github.io/cv/)
* **Direct Contact:** [alexisreal@gmail.com](mailto:alexisreal@gmail.com)
* **Investigation Background:** Based on the forensic investigation directed by the author during his tenure as Computer Systems Administrator at the Institute of Physics and Mathematics (IFM), Universidad Michoacana de San Nicolás de Hidalgo (UMSNH).
* **License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) (Open digital edition, published without commercial ISBN).

---

## Direct PDF Downloads

* **[English Edition PDF (linux-forensics-a-real-case.pdf)](linux-forensics-a-real-case.pdf)** — 173 pages, complete English translation, translated TikZ diagrams, full logs, and coordinated back cover.
* **[Spanish Edition PDF (linux-forensics-caso-real.pdf)](linux-forensics-caso-real.pdf)** — 181 pages, original Spanish text, complete technical apparatus, and forensic study guide.

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
├── linux-forensics-caso-real.tex       # Master LaTeX document (Spanish Edition)
├── linux-forensics-a-real-case.tex     # Master LaTeX document (English Edition)
├── linux-forensics-caso-real.pdf       # Compiled Spanish book (181 pages)
├── linux-forensics-a-real-case.pdf     # Compiled English book (173 pages)
├── README.md                           # Dual-language repository documentation
├── README_es.md                        # Documentación complementaria en español
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
└── figures/                            # High-resolution figures, engraving & book artwork
```

---

## Building from Source

The book compiles with modern TeX engines. We recommend **Tectonic** for its zero-configuration package management and reproducibility:

```bash
# Install Tectonic (macOS via Homebrew):
brew install tectonic

# Build the English edition:
tectonic linux-forensics-a-real-case.tex

# Build the Spanish edition:
tectonic linux-forensics-caso-real.tex
```

Alternatively, you can compile using `pdflatex` or `xelatex`:

```bash
# Two passes are required to resolve cross-references and the table of contents:
pdflatex linux-forensics-a-real-case.tex
pdflatex linux-forensics-a-real-case.tex
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

<br>

---
---

<br>

# Versión en Español: Anatomía Forense de una Intrusión

**Investigación pericial de un ataque a un sistema de producción Unix/Linux (2005 – 2025)**  
*Respuesta a incidentes, memoria viva y correlación pericial de eventos*

[![Curriculum Vitae](https://img.shields.io/badge/Curriculum%20Vitae-alexisreal.github.io%2Fcv-2ea44f?style=for-the-badge&logo=github)](https://alexisreal.github.io/cv/)
[![Linux Open Source de México](https://img.shields.io/badge/Linux%20Open%20Source%20de%20M%C3%A9xico-linuxopensource.org-0078d7?style=for-the-badge&logo=linux)](https://linuxopensource.org)
[![Licencia: CC BY-SA 4.0](https://img.shields.io/badge/Licencia-CC_BY--SA_4.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by-sa/4.0/)

> [Volver a la versión principal en inglés ↑](#linux-forensics-a-real-case)

---

### Autor y Dirección Técnica

* **Autor:** **Alexis Real Santillán**  
  *Consultor en Ciberseguridad, Arquitectura Cloud e Infraestructura Crítica.*
* **Dirección Técnica:** CTO en [**Linux Open Source de México**](https://linuxopensource.org) ([linuxopensource.org](https://linuxopensource.org))
* **Curriculum Vitae y Portafolio:** [**https://alexisreal.github.io/cv/**](https://alexisreal.github.io/cv/)
* **Contacto directo:** [alexisreal@gmail.com](mailto:alexisreal@gmail.com)
* **Contexto institucional:** Basado en la investigación pericial dirigida durante su periodo como Administrador de Sistemas en el Instituto de Física y Matemáticas (IFM), Universidad Michoacana de San Nicolás de Hidalgo (UMSNH).
* **Licencia de publicación:** [Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) (Publicación digital abierta, sin registro ISBN comercial).

---

## Descarga Directa de Libros en PDF

* **[PDF Edición en Español (linux-forensics-caso-real.pdf)](linux-forensics-caso-real.pdf)** — 181 páginas, texto original en español, aparato pericial completo y guía de estudio.
* **[PDF English Edition (linux-forensics-a-real-case.pdf)](linux-forensics-a-real-case.pdf)** — 173 páginas, traducción íntegra al inglés con diagramas TikZ y contraportada coordinada.

---

## Propósito Formativo y Editorial

Esta obra ha sido estructurada como un **manual y caso de estudio de referencia formativa para la disciplina de Análisis Forense Digital y Respuesta a Incidentes (DFIR)**. Combina el rigor técnico y la evidencia material de un caso real ocurrido en un servidor departamental de producción con un aparato pedagógico diseñado para estudiantes, analistas y peritos informáticos.

El libro se alinea formalmente con las directrices de los estándares internacionales:
* **ISO/IEC 27037:2012:** Directrices para la identificación, recolección, adquisición y preservación de evidencia digital.
* **NIST SP 800-86:** Guía de integración de técnicas forenses en la respuesta a incidentes.
* **RFC 5737 y RFC 2606:** Anonimización estandarizada de direcciones IP (`192.0.2.0/24`) y dominios preservando las relaciones de subred y la correlación pericial.

---

## Compilación desde Código Fuente

El proyecto compila directamente con el motor moderno **Tectonic** o con `pdflatex` / `xelatex`:

```bash
# Compilar edición en español:
tectonic linux-forensics-caso-real.tex

# Compilar edición en inglés:
tectonic linux-forensics-a-real-case.tex
```

---

## Componentes Didácticos Destacados

* **Cajas de Perspectiva Histórica (`perspectiva20`):** Recuadros que contrastan cómo se resolvía un problema en 2004/2005 frente a las tecnologías contemporáneas (EDR, Volatility 3, eBPF y arquitecturas Zero Trust).
* **Alertas de Integridad (`advertencia`):** Indicadores de técnicas antiforense (*anti-forensics*) y precauciones periciales en caliente.
* **Retos de Investigación Pericial (`retoforense`):** Preguntas y ejercicios prácticos de deducción pericial intercalados en los capítulos clave.
* **Diagramas Vectoriales:** Topologías de red y líneas de tiempo de ataque compuestas en alta resolución con TikZ.
* **Bitácoras Auténticas Anotadas:** Sesiones de consola, capturas de sniffer, contabilidad de procesos (acct) y metadatos de inodos preservados íntegramente.

---

## Créditos Editoriales y Asistencia Técnica

* **Obra original:** Escrita y concebida en idioma español por Alexis Real Santillán.
* **Traducción al inglés:** Realizada con la asistencia de Google Gemini.
* **Ilustraciones técnicas y diseño tipográfico:** Los diagramas vectoriales de arquitectura TikZ, el diseño de la contraportada y las revisiones tipográficas y de estilo en ambas ediciones contaron con la asistencia de Google Gemini.

---

## Licencia de Publicación

Esta obra se distribuye bajo una licencia internacional **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)**. Se autoriza su reproducción, distribución y divulgación académica, comercial o profesional citando debidamente la autoría bajo los mismos términos de licenciamiento.
