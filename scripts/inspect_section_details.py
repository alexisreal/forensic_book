with open("/Users/alexis/work/reporte-forense/original/reporte-publico-original.tex", "r", encoding="latin1") as f:
    lines = f.readlines()

def print_section_details(start, end, title):
    content = lines[start-1:end-1]
    non_empty = [l.strip() for l in content if l.strip()]
    verbatims = [i for i, l in enumerate(content) if "\\begin{verbatim}" in l]
    print(f"\n==================================================")
    print(f"TITLE: {title} (Lines {start}-{end}, Total: {len(content)})")
    print(f"Non-empty lines: {len(non_empty)}, Verbatim blocks: {len(verbatims)}")
    print("Intro text sample:")
    for l in non_empty[:5]:
        if not l.startswith("\\"):
            print("  ", l[:100])

# Inspect major blocks
print_section_details(115, 831, "Reporte (Detección inicial)")
print_section_details(832, 1400, "Contenido y función de archivos y programas")
print_section_details(1401, 2303, "Monitoreo de actividad de los usuarios")
print_section_details(2304, 2918, "Análisis post-mortem & Sistemas de referencia")
print_section_details(2919, 2998, "Búsqueda con antivirus")
print_section_details(2999, 3253, "Creación de líneas de tiempo")
print_section_details(3254, 4124, "Revisión de bitácoras del sistema")
print_section_details(4125, 4732, "Revisión de las cuentas involucradas")
print_section_details(4733, 4818, "Recuperación de archivos eliminados")
print_section_details(4819, 5001, "Correlación con otros sistemas")
print_section_details(5002, 5365, "Servidor de correo y Open Web Mail")
print_section_details(5366, 5404, "Atributos especiales en archivos")
print_section_details(5405, 5504, "Conclusiones")
