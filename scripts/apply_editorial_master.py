#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
apply_editorial_master.py
Ejecuta la corrección de estilo, ortotipografía, maquetación de galera y
estructuración jerárquica de secciones sobre todos los capítulos del libro.
"""

import os
import re

BASE_DIR = "/Users/alexis/work/reporte-forense"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

# Import the copy edit rules
from copy_edit_rules import apply_copy_editing_to_prose

def process_chapter_file(filepath, chapter_post_processor=None):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by \begin{lstlisting}... \end{lstlisting}
    parts = re.split(r"(\\begin\{lstlisting\}(?:\[.*?\])?.*?\\end\{lstlisting\})", content, flags=re.DOTALL)
    new_parts = []
    for part in parts:
        if part.startswith(r"\begin{lstlisting}"):
            # Code block: do not apply prose regexes, only normalize clean end
            new_parts.append(part)
        else:
            # Prose text: apply copy-editing, ortotypography and grammar
            cleaned_prose = apply_copy_editing_to_prose(part)
            new_parts.append(cleaned_prose)

    result = "".join(new_parts)
    if chapter_post_processor:
        result = chapter_post_processor(result)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Polished: {os.path.basename(filepath)}")

# Custom post-processors for chapters that need structural headings and sectioning
def polish_cap03(text):
    # Cap 03 had \section*{Reporte}
    text = text.replace(r"\section*{Reporte}", r"\section{Detección Inicial: Archivos con Permisos SUID y SGID}")
    
    # Add section before system directories
    text = re.sub(
        r"En seguida se hizo una búsqueda de archivos que pertenecieran a\s+usuarios distintos de root",
        r"\\section{Presencia Anómala en Directorios del Sistema}\n\nEn seguida se procedió a buscar archivos que pertenecieran a usuarios distintos de \\texttt{root}",
        text
    )
    
    # Add section before bash history
    text = re.sub(
        r"Como estos archivos no nos dan información actual de la actividad",
        r"\\section{Auditoría y Análisis de Historiales de Comandos}\n\nDado que los registros estáticos no proporcionaban información en tiempo real sobre la actividad",
        text
    )
    
    # Add subsection before /dev inspection
    text = re.sub(
        r"Se procedió a revisar el directorio \\texttt\{/dev\}",
        r"\\subsection{Inspección de Artefactos Ocultos en \\texttt{/dev}}\n\nSe procedió a revisar el directorio \\texttt{/dev}",
        text
    )
    
    return text

def polish_cap04(text):
    # Cap 04: Contenido y función de archivos y programas
    text = text.replace(
        r"\section{Contenido y función de archivos y programas}",
        r"\section{Inventario y Función de Binarios Sospechosos en \texttt{/dev}}"
    )
    
    # Add section for IRC bots
    text = re.sub(
        r"Se procedió a analizar el contenido del archivo.*energyb",
        r"\\section{Análisis de los Bots IRC: Energyb y psyBNC}\n\nSe procedió a analizar el contenido del bot \\texttt{energyb}",
        text
    )
    
    # Add section for sniffers
    text = re.sub(
        r"El archivo \s*\\texttt\{/dev/ptyp/dsniff\}",
        r"\\section{Herramientas de Espionaje y Sniffers de Red}\n\nEl archivo \\texttt{/dev/ptyp/dsniff}",
        text
    )
    
    return text

def polish_cap05(text):
    # Cap 05: Monitoreo de actividad
    text = text.replace(
        r"\section{Monitoreo de actividad de los usuarios}",
        r"\section{Supervisión Activa y Registro de Conexiones}"
    )
    
    # Add section for su root and privilege escalation
    text = re.sub(
        r"El usuario duende intentó en varias ocasiones",
        r"\\section{Intentos de Elevación de Privilegios e Interacción con el Sistema}\n\nEl usuario \\texttt{duende} intentó en reiteradas ocasiones",
        text
    )
    
    return text

def polish_cap06(text):
    # Cap 06 had no sections!
    intro_pattern = r"Primero se revisaron los programas reportados por \\texttt\{chkrootkit\}"
    replacement = r"\\section{Cotejo de Binarios con chkrootkit y Base de Datos RPM}\n\nPrimero se revisaron los programas reportados por la utilidad \\texttt{chkrootkit}"
    text = re.sub(intro_pattern, replacement, text)
    
    # Add section for specific binaries
    text = re.sub(
        r"\\texttt\{/bin/ps\}",
        r"\\subsection{Análisis Detallado del Binario \\texttt{/bin/ps}}\n\n\\noindent\\textbf{Ruta del archivo:} \\texttt{/bin/ps}",
        text
    )
    text = re.sub(
        r"\\texttt\{/bin/ls\}",
        r"\\subsection{Análisis Detallado del Binario \\texttt{/bin/ls}}\n\n\\noindent\\textbf{Ruta del archivo:} \\texttt{/bin/ls}",
        text
    )
    text = re.sub(
        r"\\texttt\{/bin/netstat\}",
        r"\\subsection{Análisis Detallado del Binario \\texttt{/bin/netstat}}\n\n\\noindent\\textbf{Ruta del archivo:} \\texttt{/bin/netstat}",
        text
    )
    
    return text

def polish_cap07(text):
    text = text.replace(
        r"\section{Búsqueda y análisis de programas troyanizados usando antivirus}",
        r"\section{Escaneo Heurístico y Detección de Firmas de Malware}"
    )
    text = text.replace(
        r"\section{Atributos especiales en archivos del sistema}",
        r"\section{Persistencia Mediante Atributos Inmutables de Ext2 (\texttt{chattr +i})}"
    )
    return text

def polish_cap08(text):
    text = text.replace(
        r"\section{Creación de líneas de tiempo}",
        r"\section{Reconstrucción Cronológica del Sistema de Archivos (\textit{Timeline Analysis})}"
    )
    return text

def polish_cap09(text):
    text = text.replace(
        r"\section{Revisión de las bitácoras del sistema}",
        r"\section{Auditoría de Bitácoras del Sistema (\texttt{syslog}, \texttt{secure} y \texttt{xferlog})}"
    )
    return text

def polish_cap10(text):
    text = text.replace(
        r"\section{Revisión de las cuentas involucradas}",
        r"\section{Inspección Forense de Directorios de Cuentas Comprometidas}"
    )
    return text

def polish_cap11(text):
    text = text.replace(
        r"\section{Recuperación de archivos eliminados del sistema}",
        r"\section{Recuperación de Inodos Huérfanos y Datos No Asignados (\textit{Carving})}"
    )
    return text

def polish_cap12(text):
    text = text.replace(
        r"\section{Correlación con otros sistemas involucrados}",
        r"\section{Movimiento Lateral y Vectores de Confianza Multisistema}"
    )
    return text

def polish_cap13(text):
    text = text.replace(
        r"\section{Bitácoras en el servidor de correo}",
        r"\section{Auditoría de Servicios de Correo Electrónico (POP3 y SMTP)}"
    )
    text = text.replace(
        r"\section{Revisión de la actividad dentro del programa lector de correo}",
        r"\section{Análisis de Sesiones y Vulnerabilidades en OpenWebMail}"
    )
    return text

def polish_cap14(text):
    text = text.replace(
        r"\section{Conclusiones}",
        r"\section{Dictamen Forense: Doble Intrusión y Atribución Pericial}"
    )
    return text

processors = {
    "cap03_deteccion_en_vivo.tex": polish_cap03,
    "cap04_siembra_servicios_malware.tex": polish_cap04,
    "cap05_monitoreo_usuarios.tex": polish_cap05,
    "cap06_analisis_referencia_rpm.tex": polish_cap06,
    "cap07_antivirus_rootkits.tex": polish_cap07,
    "cap08_lineas_tiempo_mactime.tex": polish_cap08,
    "cap09_mineria_bitacoras.tex": polish_cap09,
    "cap10_cuentas_comprometidas.tex": polish_cap10,
    "cap11_recuperacion_archivos_borrados.tex": polish_cap11,
    "cap12_correlacion_multisistema.tex": polish_cap12,
    "cap13_servidor_correo_webmail.tex": polish_cap13,
    "cap14_veredicto_y_atribucion.tex": polish_cap14,
}

if __name__ == "__main__":
    for fname in sorted(os.listdir(CHAPTERS_DIR)):
        if fname.endswith(".tex") and fname not in ["cap01_entorno_tecnologico.tex", "cap02_metodologia_forense.tex", "cap15_retrospectiva_20_anios.tex"]:
            fpath = os.path.join(CHAPTERS_DIR, fname)
            proc = processors.get(fname, None)
            process_chapter_file(fpath, proc)
    print("Editorial and galley proofing pass completed across all chapters!")
