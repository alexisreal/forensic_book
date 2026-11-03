import os

BASE_DIR = "/Users/alexis/work/reporte-forense/chapters"

# Fix cap03
cap03_path = os.path.join(BASE_DIR, "cap03_deteccion_en_vivo.tex")
with open(cap03_path, "r", encoding="utf-8") as f:
    text3 = f.read()

text3 = text3.replace(
    r"\centerline {$------------------------------------------------------------------------------------------------------------------------------------$}",
    r"\vspace{1em}"
)
text3 = text3.replace("que los creo no como", "que los creó, no como")
text3 = text3.replace("Accesó a \\texttt{/var/mail}", "Accedió a \\texttt{/var/mail}")
text3 = text3.replace("Se trato de ver una imagen", "Se trató de visualizar una imagen")

with open(cap03_path, "w", encoding="utf-8") as f:
    f.write(text3)
print("Updated cap03_deteccion_en_vivo.tex")

# Fix cap04
cap04_path = os.path.join(BASE_DIR, "cap04_siembra_servicios_malware.tex")
with open(cap04_path, "r", encoding="utf-8") as f:
    text4 = f.read()

text4 = text4.replace("Se revisara ahora", "Se revisará ahora")
text4 = text4.replace("Se estudiaran primero", "Se estudiarán primero")
text4 = text4.replace("mostraran algunas como muestra", "se mostrarán algunas como muestra")

with open(cap04_path, "w", encoding="utf-8") as f:
    f.write(text4)
print("Updated cap04_siembra_servicios_malware.tex")

# Fix cap11
cap11_path = os.path.join(BASE_DIR, "cap11_recuperacion_archivos_borrados.tex")
with open(cap11_path, "r", encoding="utf-8") as f:
    text11 = f.read()

text11 = text11.replace("Se recupero el contenido", "Se recuperó el contenido")

with open(cap11_path, "w", encoding="utf-8") as f:
    f.write(text11)
print("Updated cap11_recuperacion_archivos_borrados.tex")
