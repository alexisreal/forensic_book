import os

BASE_DIR = "/Users/alexis/work/reporte-forense/chapters"

# 1. Update cap03
cap03_file = os.path.join(BASE_DIR, "cap03_deteccion_en_vivo.tex")
with open(cap03_file, "r", encoding="utf-8") as f:
    text3 = f.read()

reto3 = """
\\begin{retoforense}[Reto Pericial 1: Auditoría de Permisos SUID y Triage en Vivo]
Suponga que durante una respuesta a incidentes en un servidor GNU/Linux localiza un ejecutable en \\texttt{/tmp/run} con permisos \\texttt{-rwsr-xr-x} perteneciente a \\texttt{root}:
\\begin{enumerate}
    \\item ¿Qué comandos de inspección binaria utilizaría para examinar el archivo de forma pasiva sin arriesgar la ejecución de código malicioso?
    \\item ¿Cómo determinaría mediante el comando \\texttt{stat} el número de inodo y si el archivo mantiene enlaces duros (\\textit{hard links}) en otras ramas del disco?
    \\item Si revoca preventivamente el bit especial con \\texttt{chmod u-s /tmp/run}, ¿cuál de las tres marcas temporales del inodo (\\textit{mtime}, \\textit{atime} o \\textit{ctime}) se actualizará en ese instante y cuál permanecerá intacta?
\\end{enumerate}
\\end{retoforense}
"""

if "Reto Pericial 1" not in text3:
    text3 = text3.replace(
        "Aunque la administración procedió de inmediato a revocar los permisos SUID para mitigar el riesgo de elevación de privilegios inmediata, la gravedad del hallazgo exigió la apertura formal de una investigación pericial profunda.",
        "Aunque la administración procedió de inmediato a revocar los permisos SUID para mitigar el riesgo de elevación de privilegios inmediata, la gravedad del hallazgo exigió la apertura formal de una investigación pericial profunda.\n" + reto3
    )
    with open(cap03_file, "w", encoding="utf-8") as f:
        f.write(text3)
    print("Added Reto 1 to cap03.")

# 2. Update cap06
cap06_file = os.path.join(BASE_DIR, "cap06_analisis_referencia_rpm.tex")
with open(cap06_file, "r", encoding="utf-8") as f:
    text6 = f.read()

reto6 = """
\\begin{retoforense}[Reto Pericial 2: Análisis Binario y Puertas Traseras]
Si un intruso altera el código de \\texttt{/bin/ps} para que ignore procesos específicos y abra una shell privilegiada cuando se ejecuta bajo un argumento secreto:
\\begin{enumerate}
    \\item ¿Por qué la verificación con \\texttt{rpm -V} o \\texttt{debsums} revelará la anomalía incluso si el intruso utilizó \\texttt{touch} para igualar la fecha de modificación con el archivo original?
    \\item ¿Qué técnica pericial estática permite descubrir las rutas fijas codificadas (como \\texttt{/dev/.libpt}) sin requerir el desensamblado completo en lenguaje ensamblador?
\\end{enumerate}
\\end{retoforense}
"""
if "Reto Pericial 2" not in text6:
    text6 = text6.replace(
        "3. \\textbf{Firma del kit de desarrollo:} La etiqueta RCS \\texttt{\\$Id: ps.c,v 1.11 2001/09/03 Exp \\$} vinculó formalmente el binario con el código fuente del kit \\textit{Linux Rootkit versión 5} (LRK5), ampliamente distribuido en foros clandestinos en la época.\n\\end{enumerate}",
        "3. \\textbf{Firma del kit de desarrollo:} La etiqueta RCS \\texttt{\\$Id: ps.c,v 1.11 2001/09/03 Exp \\$} vinculó formalmente el binario con el código fuente del kit \\textit{Linux Rootkit versión 5} (LRK5), ampliamente distribuido en foros clandestinos en la época.\n\\end{enumerate}\n" + reto6
    )
    with open(cap06_file, "w", encoding="utf-8") as f:
        f.write(text6)
    print("Added Reto 2 to cap06.")

# 3. Update cap08
cap08_file = os.path.join(BASE_DIR, "cap08_lineas_tiempo_mactime.tex")
with open(cap08_file, "r", encoding="utf-8") as f:
    text8 = f.read()

reto8 = """
\\begin{retoforense}[Reto Pericial 3: Detección de Falsificación de Marcas de Tiempo (Timestomping)]
Un atacante descarga un archivo malicioso el 15 de mayo y ejecuta \\texttt{touch -d \"2001-01-01 12:00:00\" /bin/backdoor}:
\\begin{enumerate}
    \\item Al generar la línea de tiempo con \\texttt{mactime}, ¿en qué posición cronológica figurará la marca de modificación (\\textit{mtime}) y en cuál la de cambio de metadatos (\\textit{ctime})?
    \\item Explique por qué el valor de \\textit{ctime} no puede ser manipulado directamente a través de llamadas de usuario en un sistema de archivos estándar de Linux y cómo esta discrepancia prueba judicialmente la manipulación maliciosa.
\\end{enumerate}
\\end{retoforense}
"""
if "Reto Pericial 3" not in text8:
    text8 += "\n" + reto8
    with open(cap08_file, "w", encoding="utf-8") as f:
        f.write(text8)
    print("Added Reto 3 to cap08.")
