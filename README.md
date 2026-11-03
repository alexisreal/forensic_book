# Anatomía Forense de una Intrusión

**Investigación pericial de un ataque a un sistema de producción Unix/Linux (2005 - 2025)**

* **Autor:** Alexis Real Santillán
* **Colaboración original:** Jonatan Soffer Hernández (Linux OpenSource de México S.A. de C.V.)
* **Afiliación histórica:** Instituto de Física y Matemáticas, Universidad Michoacana de San Nicolás de Hidalgo (UMSNH)
* **Licencia de publicación:** [Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Propósito Formativo y Editorial

Esta obra ha sido estructurada como un **manual y caso de estudio de referencia formativa para la disciplina de Análisis Forense Digital y Respuesta a Incidentes (DFIR)**. Combina el rigor técnico y la evidencia material de un caso real ocurrido en un servidor departamental de producción con un aparato pedagógico diseñado para estudiantes, analistas y peritos informáticos.

El libro se alinea formalmente con las directrices de los estándares internacionales **ISO/IEC 27037:2012** (Directrices para la identificación, recolección, adquisición y preservación de evidencia digital) y **NIST SP 800-86** (Guía de integración de técnicas forenses en la respuesta a incidentes).

---

## Estructura Modular de la Obra

```
reporte-forense/
├── main.tex                            # Archivo maestro compilable
├── config/
│   └── preamble.tex                    # Tipografía B5, cajas tcolorbox, listings y estilos
├── frontmatter/
│   ├── portada.tex                     # Portada editorial formal
│   ├── creditos.tex                    # Página legal, licencia CC y anonimización RFC 5737
│   ├── prefacio.tex                    # Prefacio: "Veinte Años Después (2005-2025)"
│   ├── resumen.tex                     # Resumen ejecutivo pericial
│   └── guia_estudio.tex                # Guía didáctica, axiomas forenses y matriz NIST
├── chapters/
│   ├── cap01_entorno_tecnologico.tex   # Hardware (Pentium III), servicios y topología
│   ├── cap02_metodologia_forense.tex   # Cadena de custodia, clonación y taxonomía de herramientas
│   ├── cap03_deteccion_en_vivo.tex     # Detección temprana de SUID/SGID y registros de Midnight Commander
│   ├── cap04_siembra_servicios_malware.tex # Bots IRC (Energyb, psyBNC) y exfiltración con popclean
│   ├── cap05_monitoreo_usuarios.tex    # Vigilancia pasiva, Process Accounting (acct) y sesiones
│   ├── cap06_analisis_referencia_rpm.tex # Análisis diferencial y desensamblado de /bin/ps y /bin/netstat
│   ├── cap07_antivirus_rootkits.tex    # Gusano Unix/RST.A y atributos inmutables de Ext2 (+i/+a)
│   ├── cap08_lineas_tiempo_mactime.tex # Líneas de tiempo TCT (mactime) y el "momento cero" de la intrusión
│   ├── cap09_mineria_bitacoras.tex     # Minería de auth.log, xferlog (FTP) y correlación temporal
│   ├── cap10_cuentas_comprometidas.tex # Perfil proa, directorio "..." y bot EnergyMech
│   ├── cap11_recuperacion_archivos_borrados.tex # File carving con unrm y marcador lingüístico ("algo")
│   ├── cap12_correlacion_multisistema.tex # Movimiento lateral hacia victima2 y saltos de red
│   ├── cap13_servidor_correo_webmail.tex # El servidor io, vector de abuso interno y OpenWebMail
│   ├── cap14_veredicto_y_atribucion.tex # Síntesis pericial: intrusión externa vs espía interno
│   └── cap15_retrospectiva_20_anios.tex # DFIR 2005 vs 2025: evolución técnica y lecciones universales
├── appendices/
│   ├── apendice_a_iocs.tex             # Catálogo de Indicadores de Compromiso (IoCs) y rutas
│   ├── apendice_b_bitacoras_completas.tex # Registros y transcripciones de auditoría
│   ├── apendice_c_glosario.tex         # Glosario de herramientas y conceptos clásicos de Unix
│   ├── apendice_d_comandos_forenses.tex # Cheat sheet de comandos forenses en consola GNU/Linux
│   └── apendice_e_cadena_custodia_modelo.tex # Plantilla formal de cadena de custodia ISO/IEC 27037
├── biblio/
│   ├── bibliografia.tex                # Entorno thebibliography estandarizado
│   └── referencias.bib                 # Entradas BibTeX normalizadas
├── scripts/                            # Scripts de verificación y auditoría automatizada
└── original/                           # Respaldo intacto del manuscrito original de 2005
```

---

## Componentes Didácticos Destacados

* **Cajas de Perspectiva Histórica (`perspectiva20`):** Recuadros que contrastan cómo se resolvía un problema en 2004/2005 frente a las tecnologías contemporáneas (EDR, Volatility, Zero Trust).
* **Alertas de Integridad (`advertencia`):** Indicadores de técnicas antiforense (*anti-forensics*) y precauciones periciales en caliente.
* **Retos de Investigación Pericial (`retoforense`):** Preguntas y ejercicios prácticos de razonamiento pericial intercalados en los capítulos clave para evaluación formativa.
* **Guía Rápida de Comandos Forenses:** Resumen operativo de comandos de inspección en vivo, análisis de inodos con *The Sleuth Kit* (TSK) y líneas de tiempo.
* **Plantilla de Cadena de Custodia Judicial:** Modelo formal para la acreditación probatoria de indicios digitales.

---

## Compilación a PDF

Para compilar el libro a formato PDF:

```bash
pdflatex main.tex
pdflatex main.tex  # Segunda pasada para actualizar referencias cruzadas e índices
```
