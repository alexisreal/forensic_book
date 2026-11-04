# Anatomía Forense de una Intrusión

**Investigación pericial de un ataque a un sistema de producción Unix/Linux (2005 - 2025)**

[English Version](README.md) | **Versión en Español**

* **Autor:** Alexis Real Santillán
* **Perfil:** Consultor en Ciberseguridad, Arquitectura Cloud e Infraestructura Crítica | CTO en [Linux Open Source de México](https://linuxopensource.org)
* **Trayectoria y portafolio:** [alexisreal.github.io/cv](https://alexisreal.github.io/cv/)
* **Contexto del caso:** Basado en la investigación pericial dirigida durante su periodo como Administrador de Sistemas en el Instituto de Física y Matemáticas (UMSNH).
* **Licencia de publicación:** [Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) (Publicación digital sin registro ISBN comercial)

---

## Propósito Formativo y Editorial

Esta obra ha sido estructurada como un **manual y caso de estudio de referencia formativa para la disciplina de Análisis Forense Digital y Respuesta a Incidentes (DFIR)**. Combina el rigor técnico y la evidencia material de un caso real ocurrido en un servidor departamental de producción con un aparato pedagógico diseñado para estudiantes, analistas y peritos informáticos.

El libro se alinea formalmente con las directrices de los estándares internacionales **ISO/IEC 27037:2012** (Directrices para la identificación, recolección, adquisición y preservación de evidencia digital) y **NIST SP 800-86** (Guía de integración de técnicas forenses en la respuesta a incidentes).

---

## Estructura Modular de la Obra

El repositorio incluye dos ediciones completas, paralelas y consistentes:
* **Edición en Español:** Compilable desde `main.tex` $\to$ `main.pdf`.
* **Edición en Inglés (*Linux Forensics: A Real Case*):** Compilable desde `main_en.tex` $\to$ `main_en.pdf`.

```
reporte-forense/
├── main.tex                            # Archivo maestro compilable (Español)
├── main_en.tex                         # Master compilable file (English Edition)
├── main.pdf                            # PDF compilado (Español, 181 páginas)
├── main_en.pdf                         # PDF compilado (Inglés, 173 páginas)
├── config/
│   ├── preamble.tex                    # Configuración tipográfica en español
│   └── preamble_en.tex                 # English typographic & callout preamble
├── frontmatter/ & frontmatter_en/
│   ├── portada.tex                     # Portada editorial formal
│   ├── contraportada.tex               # Contraportada editorial coordinada (sin ISBN)
│   ├── creditos.tex                    # Página legal, licencia CC y atribución
│   ├── dedicatoria.tex                 # Dedicatoria formal
│   ├── prefacio.tex                    # Prefacio: 20 años de evolución Unix
│   ├── resumen.tex                     # Resumen ejecutivo pericial
│   └── guia_estudio.tex                # Guía didáctica, axiomas forenses y matriz NIST/ISO
├── chapters/ & chapters_en/
│   ├── cap01_entorno_tecnologico.tex   # Hardware, servicios y topología departamental
│   ├── cap02_metodologia_forense.tex   # Cadena de custodia, clonación y taxonomía
│   ├── cap03_deteccion_en_vivo.tex     # Detección temprana SUID/SGID y Midnight Commander
│   ├── cap04_siembra_servicios_malware.tex # Bots IRC, sniffer dsniff y credenciales
│   ├── cap05_monitoreo_usuarios.tex    # Vigilancia activa, Process Accounting (acct) y sesiones
│   ├── cap06_analisis_referencia_rpm.tex # Análisis diferencial y rootkit Suckit v1.3b
│   ├── cap07_antivirus_rootkits.tex    # Gusano Unix/RST.A y atributos inmutables Ext2 (+i/+a)
│   ├── cap08_lineas_tiempo_mactime.tex # Líneas de tiempo TCT (mactime) y "hora cero"
│   ├── cap09_mineria_bitacoras.tex     # Minería de auth.log, daemon.log, wtmp y xferlog
│   ├── cap10_cuentas_comprometidas.tex # Cuentas proa, zena, zopilote, o0o.tar y dump.sh
│   ├── cap11_recuperacion_archivos_borrados.tex # Inodos huérfanos, carving y pista "algo"
│   ├── cap12_correlacion_multisistema.tex # Movimiento lateral hacia atlas (pivoting)
│   ├── cap13_servidor_correo_webmail.tex # Servidor io, intrusión admin y OpenWebMail
│   ├── cap14_veredicto_y_atribucion.tex # Síntesis pericial: intrusión externa vs espía interno
│   └── cap15_retrospectiva_20_anios.tex # Retrospectiva DFIR 2005-2025: RAM, eBPF y Cloud
├── appendices/ & appendices_en/
│   ├── apendice_a_iocs.tex             # Catálogo de indicadores de compromiso (IoCs)
│   ├── apendice_b_bitacoras_completas.tex # Transcripción anotada de bitácoras periciales
│   ├── apendice_c_glosario.tex         # Glosario técnico de más de 40 términos DFIR
│   ├── apendice_d_comandos_forenses.tex # Guía rápida de comandos forenses de consola
│   └── apendice_e_cadena_custodia_modelo.tex # Formato modelo de cadena de custodia ISO 27037
├── biblio/
│   ├── bibliografia.tex                # Bibliografía en español
│   └── bibliografia_en.tex             # English bibliography
└── img/                                # Diagramas e ilustraciones (sabueso_color.jpg)
```

---

## Compilación del Documento

El proyecto está optimizado para compilar directamente con el motor moderno **Tectonic** (o XeLaTeX / pdfLaTeX con soporte de fuentes Type 1 y microtype):

```bash
# Compilar edición en español:
tectonic main.tex

# Compilar edición en inglés:
tectonic main_en.tex
```

---

## Componentes Didácticos Destacados

* **Cajas de Perspectiva Histórica (`perspectiva20`):** Recuadros que contrastan cómo se resolvía un problema en 2004/2005 frente a las tecnologías contemporáneas (EDR, Volatility, Zero Trust).
* **Alertas de Integridad (`advertencia`):** Indicadores de técnicas antiforense (*anti-forensics*) y precauciones periciales en caliente.
* **Retos de Investigación Pericial (`retoforense`):** Preguntas y ejercicios prácticos de razonamiento pericial intercalados en los capítulos clave para evaluación formativa.
* **Guía Rápida de Comandos Forenses:** Resumen operativo de comandos de inspección en vivo, análisis de inodos con *The Sleuth Kit* (TSK) y líneas de tiempo.
* **Plantilla de Cadena de Custodia Judicial:** Modelo formal para la acreditación probatoria de indicios digitales.

---

## Créditos y Asistencia Técnica

* **Obra original:** Escrita y concebida en idioma español por Alexis Real Santillán.
* **Traducción al inglés:** Realizada con la asistencia de Google Gemini.
* **Diagramas y correcciones tipográficas:** Ilustraciones vectoriales TikZ, diagramas de arquitectura técnica y correcciones tipográficas de ambas ediciones asistidas por Google Gemini.
