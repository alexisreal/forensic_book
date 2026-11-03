# Anatomía Forense de una Intrusión

**Investigación pericial de un ataque a un sistema de producción Unix/Linux (2005)**

* **Autor:** Alexis Real Santillán
* **Colaboración original:** Jonatan Soffer Hernández (Linux OpenSource de México S.A. de C.V.)
* **Afiliación histórica:** Instituto de Física y Matemáticas, Universidad Michoacana de San Nicolás de Hidalgo (UMSNH)
* **Licencia de publicación:** [Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Descripción del Proyecto

Este repositorio contiene la edición revisada, modernizada y adaptada en formato de **libro técnico monográfico** del informe pericial redactado originalmente en enero de 2005.

El documento investiga en profundidad una intrusión en un servidor departamental de producción con arquitectura Intel Pentium III sobre Red Hat Linux, revelando la convergencia de dos incidentes independientes:
1. Una intrusión oportunista externa aprovechando contraseñas débiles en el servicio FTP para alojar bots de IRC (*eggdrop*, *psyBNC*, *energyb*).
2. Un ataque concurrente por parte de un actor interno con acceso a las instalaciones físicas del edificio, quien intentó desplegar *rootkits*, modificar atributos inmutables (`chattr +i`) y capturar credenciales de administración mediante *sniffers* de red.

---

## Estructura del Libro

El proyecto ha sido desglosado en una arquitectura modular:

```
reporte-forense/
├── main.tex                    # Archivo maestro compilable
├── config/
│   └── preamble.tex            # Paquetes, tipografía (B5), estilos de listados y cajas
├── frontmatter/
│   ├── portada.tex             # Portada editorial
│   ├── creditos.tex            # Página legal, licencia CC y declaración de anonimización RFC 5737
│   ├── prefacio.tex            # Prefacio retrospectivo "20 Años Después"
│   └── resumen.tex             # Resumen pericial ejecutivo
├── chapters/
│   ├── cap01_entorno_tecnologico.tex
│   ├── cap02_metodologia_forense.tex
│   ├── cap03_deteccion_en_vivo.tex
│   ├── cap04_siembra_servicios_malware.tex
│   ├── cap05_monitoreo_usuarios.tex
│   ├── cap06_analisis_referencia_rpm.tex
│   ├── cap07_antivirus_rootkits.tex
│   ├── cap08_lineas_tiempo_mactime.tex
│   ├── cap09_mineria_bitacoras.tex
│   ├── cap10_cuentas_comprometidas.tex
│   ├── cap11_recuperacion_archivos_borrados.tex
│   ├── cap12_correlacion_multisistema.tex
│   ├── cap13_servidor_correo_webmail.tex
│   ├── cap14_veredicto_y_atribucion.tex
│   └── cap15_retrospectiva_20_anios.tex
├── appendices/
│   ├── apendice_a_iocs.tex     # Catálogo de Indicadores de Compromiso (IoCs)
│   ├── apendice_b_bitacoras_completas.tex # Registros y transcripciones de auditoría
│   └── apendice_c_glosario.tex # Glosario de herramientas y conceptos forenses clásicos
├── biblio/
│   ├── bibliografia.tex        # Entorno thebibliography estandarizado
│   └── referencias.bib         # Entradas BibTeX normalizadas
├── scripts/                    # Scripts de conversión, anonimización e inspección
└── original/                   # Respaldo intacto del archivo original de 2005
```

---

## Compilación a PDF

Para compilar el libro a formato PDF:

```bash
pdflatex main.tex
pdflatex main.tex  # Segunda pasada para generar la tabla de contenidos
```

O utilizando `latexmk`:

```bash
latexmk -pdf main.tex
```

También es compatible al 100% con plataformas como Overleaf.
