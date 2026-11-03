#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
convert_to_book.py
Genera todos los capítulos del libro estructurado a partir del reporte pericial original.
"""

import os
import re
from build_ip_map import build_ip_anonymizer

ORIGINAL_FILE = "/Users/alexis/work/reporte-forense/original/reporte-publico-original.tex"
BASE_DIR = "/Users/alexis/work/reporte-forense"

with open(ORIGINAL_FILE, "r", encoding="latin1") as f:
    RAW_LINES = f.readlines()

FULL_RAW_TEXT = "".join(RAW_LINES)
IP_MAP = build_ip_anonymizer(FULL_RAW_TEXT)

def anonymize_text(text):
    for real_ip, fake_ip in IP_MAP.items():
        text = text.replace(real_ip, fake_ip)
    text = text.replace("xxx.xxx.xxx.1", "192.0.2.10")
    return text

def convert_accents_and_typography(text):
    replacements = [
        (r"\\'a", "á"), (r"\\'e", "é"), (r"\\'i", "í"), (r"\\'o", "ó"), (r"\\'u", "ú"),
        (r"\\'A", "Á"), (r"\\'E", "É"), (r"\\'I", "Í"), (r"\\'O", "Ó"), (r"\\'U", "Ú"),
        (r"\\~n", "ñ"), (r"\\~N", "Ñ"),
        (r'\\"u', "ü"), (r'\\"U', "Ü"),
        (r"'a", "á"), (r"'e", "é"), (r"'i", "í"), (r"'o", "ó"), (r"'u", "ú"),
        (r"'A", "Á"), (r"'E", "É"), (r"'I", "Í"), (r"'O", "Ó"), (r"'U", "Ú"),
        (r"~n", "ñ"), (r"~N", "Ñ"),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)

    text = re.sub(r"\{\\bf\s+([^}]+)\}", r"\\textbf{\1}", text)
    text = re.sub(r"\{\\em\s+([^}]+)\}", r"\\emph{\1}", text)
    text = re.sub(r"\{\\it\s+([^}]+)\}", r"\\textit{\1}", text)
    text = re.sub(r"\{\\tt\s+([^}]+)\}", r"\\texttt{\1}", text)
    text = re.sub(r"\\centerline\s*\{[-—_]{5,}\}", r"\\vspace{0.8em}\\hrulefill\\vspace{0.8em}", text)
    text = re.sub(r"\\vskip\s+\d+mm", r"\\vspace{1em}", text)
    # clean \subsection* and \subsubsection* inside raw chunks to \section or \subsection
    text = re.sub(r"\\subsection\*?\{([^}]+)\}", r"\\section{\1}", text)
    text = re.sub(r"\\subsubsection\*?\{([^}]+)\}", r"\\subsection{\1}", text)
    return text

def process_latex_content(content):
    parts = re.split(r"(\\begin\{verbatim\}.*?\\end\{verbatim\})", content, flags=re.DOTALL)
    processed_parts = []
    for part in parts:
        if part.startswith(r"\begin{verbatim}"):
            inner = part[len(r"\begin{verbatim}"):-len(r"\end{verbatim}")]
            cleaned_inner = anonymize_text(inner)
            processed_parts.append(r"\begin{lstlisting}[style=terminal]" + cleaned_inner + r"\end{lstlisting}")
        else:
            cleaned = anonymize_text(part)
            cleaned = convert_accents_and_typography(cleaned)
            processed_parts.append(cleaned)
    return "".join(processed_parts)

def slice_raw(start_1indexed, end_1indexed):
    return "".join(RAW_LINES[start_1indexed-1:end_1indexed])

def write_chapter(filename, title, intro_text, raw_content, callout_text=None, retrospectiva_text=None):
    filepath = os.path.join(BASE_DIR, "chapters", filename)
    body = process_latex_content(raw_content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"\\chapter{{{title}}}\n\n")
        if intro_text:
            f.write(intro_text.strip() + "\n\n")
        if callout_text:
            f.write(callout_text.strip() + "\n\n")
        f.write(body.strip() + "\n\n")
        if retrospectiva_text:
            f.write(retrospectiva_text.strip() + "\n")
    print(f"Created {filename}")

# CHAPTER 1: Topología y Entorno Tecnológico (L88-114)
intro_ch1 = """
El punto de partida de toda investigación pericial informática exige una caracterización minuciosa del objetivo: su arquitectura de hardware, sistema operativo, topología de red y los servicios de red expuestos al momento del incidente. En el contexto de 2004, los servidores departamentales solían asumir roles múltiples y concurrentes (correo, archivos NFS, estaciones de cómputo y entornos gráficos X11), lo que ampliaba notablemente su superficie de ataque.
"""
callout_ch1 = """
\\begin{notaforense}[Contexto de Infraestructura en 2004]
El servidor estudiado representaba el estándar de cómputo de alto rendimiento departamental a principios de la década del 2000: una arquitectura x86 monoprocesador Intel Pentium III sobre bus PCI y discos duros SCSI/IDE, enlazada mediante conmutadores Fast Ethernet (100 Mbps) a una red universitaria con direccionamiento IPv4 público directo y sin cortafuegos de aplicación intermedios.
\\end{notaforense}
"""
retrospectiva_ch1 = """
\\begin{perspectiva20}[Perspectiva 20 Años Después: Topología y Perímetro]
En 2004, era una práctica habitual conectar servidores de cómputo directamente con direcciones IP públicas sin capas de inspección profunda de paquetes ni arquitecturas de confianza cero (\\textit{Zero Trust}). Actualmente, un sistema análogo operaría dentro de una VPC privada, aislado tras pasarelas seguras, balanceadores de carga con WAF, segmentación por microperímetros y autenticación reforzada mediante llaves criptográficas basadas en hardware.
\\end{perspectiva20}
"""
raw_ch1 = slice_raw(88, 114)
write_chapter("cap01_entorno_tecnologico.tex", "Topología y Entorno Tecnológico", intro_ch1, raw_ch1, callout_ch1, retrospectiva_ch1)

# CHAPTER 2: Principios Forenses y Cadena de Custodia (L2304-2450)
intro_ch2 = """
La validez jurídica y técnica de un dictamen forense descansa en la inviolabilidad de la evidencia. Frente a una sospecha de compromiso, el perito debe resolver el dilema fundamental entre preservar el estado volátil de la máquina en funcionamiento o proceder al apagado controlado para su examen estático en laboratorio.
"""
callout_ch2 = """
\\begin{notaforense}[La Regla de Oro Forense]
Nunca se investiga directamente sobre el medio original de almacenamiento si no es estrictamente imprescindible. La clonación bit a bit y el cotejo criptográfico mediante sumas de verificación MD5 y SHA1 garantizan que el estado de la evidencia permanezca inalterado a lo largo del proceso pericial.
\\end{notaforense}
"""
retrospectiva_ch2 = """
\\begin{perspectiva20}[Perspectiva 20 Años Después: Adquisición de Memoria Volátil]
En 2004, la adquisición de memoria RAM viva estaba en una fase incipiente (herramientas como \\textit{fmem} o \\textit{dd} sobre \\texttt{/dev/mem}). Hoy en día, la captura de memoria volátil mediante herramientas como \\textit{LiME} (\\textit{Linux Memory Extractor}) y su posterior análisis con \\textit{Volatility 3} constituyen el primer paso ineludible antes de apagar cualquier sistema comprometido, permitiendo rescatar llaves criptográficas, sockets y procesos inyectados que desaparecen al apagar el equipo.
\\end{perspectiva20}
"""
raw_ch2 = slice_raw(2304, 2465)
write_chapter("cap02_metodologia_forense.tex", "Principios Forenses y Cadena de Custodia", intro_ch2, raw_ch2, callout_ch2, retrospectiva_ch2)

# CHAPTER 3: Detección Temprana y Artefactos en Vivo (L115-831)
intro_ch3 = """
La detección inicial de una intrusión suele manifestarse a través de discrepancias sutiles en la operación cotidiana del sistema. A mediados de abril de 2004, la administración de cómputo identificó la presencia de archivos con permisos especiales y propietarios no autorizados en ubicaciones reservadas al sistema. Este capítulo documenta las primeras acciones de respuesta en vivo y el inventario preliminar de artefactos anómalos.
"""
callout_ch3 = """
\\begin{notaforense}[Uso de /dev como Ocultamiento Tradicional]
El directorio \\texttt{/dev} fue históricamente el refugio predilecto de los intrusos en sistemas Unix/Linux. Dado que alberga cientos de archivos especiales de bloques y caracteres, los atacantes solían crear subdirectorios camuflados con nombres de dispositivos virtuales (como \\texttt{/dev/ptyp} o \\texttt{/dev/...}) para almacenar herramientas de compilación, sniffers y ejecutables con bit SUID activado.
\\end{notaforense}
"""
raw_ch3 = slice_raw(115, 831)
write_chapter("cap03_deteccion_en_vivo.tex", "Detección Temprana y Artefactos en Vivo", intro_ch3, raw_ch3, callout_ch3)

# CHAPTER 4: Infraestructura Parásita: Bots IRC y Malware (L832-1400)
intro_ch4 = """
Durante los primeros años del siglo XXI, la motivación primordial de los grupos de atacantes automatizados y oportunistas no era el robo de propiedad intelectual ni el secuestro de datos (\\textit{ransomware}), sino la apropiación de ancho de banda y capacidad de cómputo para gobernar redes de canales IRC. La implantación de \\textit{Eggdrop}, \\textit{psyBNC} y servidores de retransmisión clandestinos convertía servidores académicos en nodos zombis sin el consentimiento de sus administradores.
"""
raw_ch4 = slice_raw(832, 1400)
write_chapter("cap04_siembra_servicios_malware.tex", "Infraestructura Parásita: Bots IRC y Malware", intro_ch4, raw_ch4)

# CHAPTER 5: Monitoreo Activo y Análisis de Sesiones (L1401-2303)
intro_ch5 = """
Una vez descubiertos los artefactos sin que el atacante advirtiera la intervención pericial, se tomó la decisión estratégica de establecer un monitoreo encubierto. A través de la supervisión de las sesiones interactivas asociadas a la cuenta sospechosa \\texttt{duende}, el equipo de investigación pudo registrar en tiempo real las tácticas, técnicas y procedimientos (TTP) del intruso.
"""
raw_ch5 = slice_raw(1401, 2303)
write_chapter("cap05_monitoreo_usuarios.tex", "Monitoreo Activo y Análisis de Sesiones", intro_ch5, raw_ch5)

# CHAPTER 6: Análisis Diferencial con el Sistema de Referencia (L2451-2918)
intro_ch6 = """
El método de análisis forense comparativo consiste en contrastar el estado del sistema investigado contra una instalación limpia e idéntica montada en el laboratorio de referencia. En entornos GNU/Linux basados en RPM (Red Hat Package Manager), el comando \\texttt{rpm -V} permite contrastar los tamaños de archivo, fechas de modificación, atributos y sumas de verificación MD5 respecto a la base de datos oficial del distribuidor.
"""
raw_ch6 = slice_raw(2466, 2918)
write_chapter("cap06_analisis_referencia_rpm.tex", "Análisis Diferencial con el Sistema de Referencia", intro_ch6, raw_ch6)

# CHAPTER 7: Detección de Binarios Troyanizados y Rootkits (L2919-2998 + L5366-5404)
intro_ch7 = """
Los \\textit{rootkits} a nivel de espacio de usuario (\\textit{userland rootkits}) operaban reemplazando los binarios estándar de administración (como \\texttt{ps}, \\texttt{ls}, \\texttt{netstat}, \\texttt{find} y \\texttt{login}) por versiones adulteradas que filtraban deliberadamente los procesos del atacante, ocultaban directorios maliciosos y abrían puertas traseras protegidas por contraseñas predefinidas.
"""
raw_ch7 = slice_raw(2919, 2998) + "\n\n" + slice_raw(5366, 5404)
write_chapter("cap07_antivirus_rootkits.tex", "Detección de Binarios Troyanizados y Rootkits", intro_ch7, raw_ch7)

# CHAPTER 8: Cronología Forense del Sistema de Archivos (L2999-3253)
intro_ch8 = """
La reconstrucción temporal de eventos constituye la columna vertebral del análisis pericial. El sistema de archivos almacena tres marcas de tiempo críticas para cada inodo: fecha de última modificación del contenido (\\textit{mtime}), fecha de último acceso de lectura (\\textit{atime}) y fecha de cambio en los metadatos o inodo (\\textit{ctime}). Utilizando la herramienta \\texttt{mactime} de \\textit{The Coroner's Toolkit} (TCT), fue posible correlacionar con precisión de segundos cada acción ejecutada en el disco.
"""
raw_ch8 = slice_raw(2999, 3253)
write_chapter("cap08_lineas_tiempo_mactime.tex", "Cronología Forense del Sistema de Archivos", intro_ch8, raw_ch8)

# CHAPTER 9: Minería y Correlación de Bitácoras del Sistema (L3254-4124)
intro_ch9 = """
Las bitácoras de auditoría del sistema operativo (\\texttt{/var/log/messages}, \\texttt{secure}, \\texttt{wtmp}, \\texttt{xferlog}) ofrecen el testimonio cronológico de autenticaciones, conexiones externas y comandos privilegiados. En este capítulo se analizan las secuencias de eventos registradas, desentrañando además los intentos del atacante por limpiar y manipular los archivos de registro.
"""
raw_ch9 = slice_raw(3254, 4124)
write_chapter("cap09_mineria_bitacoras.tex", "Minería y Correlación de Bitácoras del Sistema", intro_ch9, raw_ch9)

# CHAPTER 10: Análisis Forense de Cuentas Comprometidas (L4125-4732)
intro_ch10 = """
La seguridad de un sistema de cómputo multiusuario es tan sólida como el eslabón más débil de su cadena de credenciales. El análisis forense de los directorios personales de los usuarios afectados reveló el mecanismo de acceso inicial y el depósito de herramientas auxiliares que permitieron la consolidación de la presencia no autorizada.
"""
raw_ch10 = slice_raw(4125, 4732)
write_chapter("cap10_cuentas_comprometidas.tex", "Análisis Forense de Cuentas Comprometidas", intro_ch10, raw_ch10)

# CHAPTER 11: Recuperación de Archivos Eliminados e Inodos Huérfanos (L4733-4818)
intro_ch11 = """
Cuando un intruso advierte la posibilidad de ser detectado o concluye una fase de su ataque, suele ejecutar comandos de borrado (\\texttt{rm -rf}) para suprimir sus herramientas y bitácoras intermedias. Sin embargo, en el sistema de archivos Ext2/Ext3, la eliminación de un archivo desasocia el inodo del directorio pero mantiene intactos los bloques de datos en el disco magnético hasta que son reutilizados por nuevas operaciones de escritura.
"""
raw_ch11 = slice_raw(4733, 4818)
write_chapter("cap11_recuperacion_archivos_borrados.tex", "Recuperación de Archivos Eliminados e Inodos Huérfanos", intro_ch11, raw_ch11)

# CHAPTER 12: Movimiento Lateral y Correlación Multisistema (L4819-5001)
intro_ch12 = """
Una intrusión rara vez permanece confinada a un único servidor cuando los sistemas comparten redes locales, montajes remotos NFS o esquemas de confianza entre cuentas de usuario. La correlación pericial con otros servidores del departamento permitió reconstruir la propagación lateral y confirmar la hipótesis sobre el origen de los accesos.
"""
raw_ch12 = slice_raw(4819, 5001)
write_chapter("cap12_correlacion_multisistema.tex", "Movimiento Lateral y Correlación Multisistema", intro_ch12, raw_ch12)

# CHAPTER 13: Vectores en el Servidor de Correo y Webmail (L5002-5365)
intro_ch13 = """
Las aplicaciones de acceso a correo web en la década del 2000, desarrolladas con frecuencia como scripts CGI en Perl o PHP sin suficiente validación de entradas ni protección contra sesiones concurrentes, representaban una superficie de ataque sumamente vulnerable. El servidor de correo departamental fue analizado minuciosamente para determinar si las intrusiones involucraron la interceptación de correspondencia electrónica.
"""
raw_ch13 = slice_raw(5002, 5365)
write_chapter("cap13_servidor_correo_webmail.tex", "Vectores en el Servidor de Correo y Webmail", intro_ch13, raw_ch13)

# CHAPTER 14: Veredicto Pericial y Síntesis del Caso (L5405-5504)
intro_ch14 = """
La fase final de toda investigación pericial consiste en integrar la totalidad de los indicios materiales, marcas de tiempo y correlaciones de red en una hipótesis concluyente que reconstruya la mecánica de los hechos y determine el grado de afectación real de la infraestructura evaluada.
"""
raw_ch14 = slice_raw(5405, 5504)
write_chapter("cap14_veredicto_y_atribucion.tex", "Veredicto Pericial y Síntesis del Caso", intro_ch14, raw_ch14)

# CHAPTER 15: Retrospectiva: 20 Años de Cómputo Forense
retrospectiva_full = """
\\chapter{Retrospectiva: 20 Años de Cómputo Forense}

Transcurridas dos décadas desde que se recolectaron los inodos y se clonaron los discos de este incidente, el campo del análisis forense digital y la respuesta a incidentes (DFIR) ha experimentado una metamorfosis radical. Reflexionar sobre este caso a la distancia permite distinguir con claridad lo efímero de lo permanente en la seguridad informática.

\\section{La Evolución Tecnológica: De la Máquina Física a la Nube Efímera}

En 2004, la investigación pericial se concebía como un procedimiento eminentemente físico:
\\begin{itemize}
    \\item \\textbf{El medio material:} La evidencia residía en platos magnéticos con sectores de 512 bytes, conectados por cables IDE de 40 u 80 hilos o controladoras SCSI. Los tiempos de transferencia se medían en megabytes por segundo y la clonación física requería horas de espera junto al gabinete del servidor.
    \\item \\textbf{El sistema operativo:} El kernel Linux 2.4/2.6 operaba con módulos monolíticos; los sistemas de archivos Ext2 carecían de bitácora transaccional (\\textit{journaling}), lo que hacía que el borrado de archivos preservara los punteros de inodos de forma predecible y facilitara el \\textit{unrm}.
    \\item \\textbf{Las herramientas del perito:} El análisis dependía de utilidades pioneras desarrolladas por figuras fundacionales como Dan Farmer y Wietse Venema (\\textit{The Coroner's Toolkit} - TCT), y los primeros trabajos de Brian Carrier con \\textit{The Sleuth Kit} (TSK) y su interfaz web \\textit{Autopsy}.
\\end{itemize}

Hoy en día, el panorama tecnológico presenta desafíos de naturaleza distinta:
\\begin{itemize}
    \\item \\textbf{La virtualización y contenedores:} Los servidores de producción ya no poseen una existencia física individualizada; residen como instancias en nubes públicas (AWS, Azure, GCP) o contenedores efímeros (Docker, Kubernetes) cuyo ciclo de vida puede ser de minutos. Cuando un contenedor es destruido, la evidencia volátil desaparece si no existen mecanismos previos de telemetría continua.
    \\item \\textbf{Sistemas de archivos modernos y cifrado:} Con Ext4, XFS, ZFS y el cifrado generalizado en reposo (LUKS), el \\textit{file carving} tradicional y la recuperación directa de bloques borrados se han tornado considerablemente más complejos.
    \\item \\textbf{La primacía de la memoria volátil:} La aparición de \\textit{Volatility} transformó la disciplina: hoy en día, no se concibe una investigación forense seria sin el volcado y análisis del espacio de memoria RAM, donde residen las inyecciones DLL/SO, los hilos de ejecución encubiertos y las claves de cifrado en uso.
\\end{itemize}

\\section{Las Lecciones Inmutables: La Psicología del Ataque}

Frente a la constante renovación de herramientas y plataformas, resulta aleccionador comprobar cómo los vectores esenciales identificados en este caso continúan manifestándose con idéntica vigencia en los incidentes modernos:

\\begin{enumerate}
    \\item \\textbf{La debilidad del factor humano en la autenticación:} El vector de entrada inicial fue una contraseña trivial en un servicio de transferencia de archivos. Veinte años después, el robo de credenciales, el relleno de credenciales (\\textit{credential stuffing}) y la reutilización de contraseñas continúan representando más del 80\\% de los accesos iniciales según los informes globales de ciberseguridad. La única respuesta efectiva contemporánea ha sido el despliegue universal de autenticación multifactor (MFA) resistente a la suplantación.
    \\item \\textbf{La amenaza interna (\\textit{Insider Threat}):} El hallazgo más inquietante de esta pericia fue la convergencia entre un atacante oportunista remoto y un actor local que intentó aprovechar el incidente para sus propios fines de espionaje. La literatura actual confirma que las amenazas internas —ya sean maliciosas o negligentes— causan el mayor impacto financiero y operativo en las organizaciones, precisamente porque el actor interno conoce la topología, los procedimientos de respuesta y la ubicación exacta de los activos críticos.
    \\item \\textbf{La persistencia y el camuflaje:} Las técnicas empleadas en 2004 (modificar atributos inmutables con \\texttt{chattr +i}, ocultar directorios bajo \\texttt{/dev}, suplantar binarios del sistema) encuentran su reflejo contemporáneo en los ataques de \\textit{Living off the Land} (LotL), donde los intrusos utilizan herramientas administrativas legítimas del propio sistema operativo (\\textit{PowerShell}, \\textit{WMI}, \\textit{eBPF}) para evadir las alertas de los antivirus y los agentes EDR.
\\end{enumerate}

\\section{Epílogo para el Investigador del Siglo XXI}

El ejercicio de la ciencia forense digital exige una disciplina intelectual que trasciende las épocas: la desconfianza metódica hacia lo evidente, el respeto estricto por la cadena de custodia, y la convicción de que en un sistema digital todo evento deja una huella imborrable.

Quien domine los fundamentos artesanales documentados en este libro —el examen directo de inodos, la lectura crítica de bitácoras y la correlación matemática de marcas de tiempo— comprenderá con profunda solvencia técnica los sistemas de defensa automatizados del presente y del porvenir.
"""

with open(os.path.join(BASE_DIR, "chapters", "cap15_retrospectiva_20_anios.tex"), "w", encoding="utf-8") as f:
    f.write(retrospectiva_full.strip() + "\n")
print("Created cap15_retrospectiva_20_anios.tex")

# APPENDICES
# Apéndice A: IoCs
apendice_a = """
\\chapter{Catálogo de Indicadores de Compromiso (IoCs)}

En este apéndice se compendian los artefactos maliciosos, rutas sospechosas y atributos de persistencia identificados durante la investigación pericial en el servidor \\texttt{victima1}.

\\section{Rutas y Binarios Clave Identificados}

\\begin{table}[h!]
\\centering
\\footnotesize
\\begin{tabular}{lll}
\\toprule
\\textbf{Ruta del Artefacto} & \\textbf{Propietario / Permisos} & \\textbf{Descripción / Función Detectada} \\\\
\\midrule
\\texttt{/dev/ptyp} & \\texttt{root:root (drwxr-xr-x)} & Directorio oculto de depósito y scripts \\\\
\\texttt{/dev/ptyp/energyb} & \\texttt{root:root (rwxr-xr-x)} & Bot IRC con soporte DCC y retransmisión \\\\
\\texttt{/dev/ptyp/psybnc} & \\texttt{root:root (rwxr-xr-x)} & Bouncer IRC para encubrimiento de conexiones \\\\
\\texttt{/usr/lib/popclean} & \\texttt{root:root (-u--ia-----)} & Binario modificado con atributo inmutable \\\\
\\texttt{/usr/local/lib/dsniff.services} & \\texttt{root:root (-u--ia-----)} & Capturador y analizador de credenciales de red \\\\
\\texttt{/tmp/...} & \\texttt{duende:duende (drwxrwxrwx)} & Directorio temporal de desempaque de malware \\\\
\\bottomrule
\\end{tabular}
\\caption{Artefactos y ejecutables sospechosos identificados en el sistema comprometido.}
\\end{table}

\\section{Atributos Especiales de Archivos del Sistema}

Varios de los ejecutables troyanizados fueron fijados con atributos especiales de Ext2 para evitar su eliminación o modificación incluso por el usuario \\texttt{root}:
\\begin{itemize}
    \\item \\textbf{Atributo inmutable (\\texttt{+i}):} Impide que el archivo sea modificado, renombrado, eliminado o sobreescrito. Solo puede removerse restableciendo explícitamente el atributo con el comando \\texttt{chattr -i}.
    \\item \\textbf{Atributo de adición únicamente (\\texttt{+a}):} Restringe la apertura del archivo únicamente para agregar información al final, bloqueando el truncamiento o borrado.
\\end{itemize}
"""
with open(os.path.join(BASE_DIR, "appendices", "apendice_a_iocs.tex"), "w", encoding="utf-8") as f:
    f.write(apendice_a.strip() + "\n")
print("Created apendice_a_iocs.tex")

# Apéndice B: Bitácoras completas
apendice_b = """
\\chapter{Transcripción y Compendio de Bitácoras}

A lo largo de la investigación forense se procesaron decenas de miles de líneas de registros de auditoría. Para mantener la legibilidad y el ritmo pedagógico de la obra, los capítulos principales incluyen únicamente los extractos y discrepancias fundamentales.

En este apéndice se preserva la estructura de los registros más representativos para fines de análisis comparativo y práctica pericial.

\\section{Estructura de Registros de Autenticación (wtmp / last)}
Los registros de conexión revelan la alternancia entre sesiones legítimas del usuario y accesos clandestinos a través de direcciones de acceso conmutado y DSL:
\\begin{lstlisting}[style=terminal]
duende   pts/2        198.51.100.61    Mon Apr 12 18:34 - 19:12  (00:38)
duende   pts/1        198.51.100.98    Mon Apr 12 19:45 - 20:22  (00:37)
duende   ftp          203.0.113.124    Tue Apr 13 02:11 - 02:15  (00:04)
duende   pts/0        198.51.100.156   Tue Apr 13 02:16 - 03:40  (01:24)
\\end{lstlisting}

\\section{Registros de Transferencia FTP (xferlog)}
El servicio FTP fue el vector primordial de descarga de paquetes comprimidos (\\texttt{.tar.gz}) que contenían el código fuente de los servidores IRC y los scripts de compilación automática.
\\begin{lstlisting}[style=terminal]
Tue Apr 13 02:12:04 2004 1 203.0.113.124 152841 /home/duende/b.tar.gz b _ i r duende ftp 0 * c
Tue Apr 13 02:14:18 2004 1 203.0.113.124 845201 /home/duende/psy.tar.gz b _ i r duende ftp 0 * c
\\end{lstlisting}
"""
with open(os.path.join(BASE_DIR, "appendices", "apendice_b_bitacoras_completas.tex"), "w", encoding="utf-8") as f:
    f.write(apendice_b.strip() + "\n")
print("Created apendice_b_bitacoras_completas.tex")

# Apéndice C: Glosario
apendice_c = """
\\chapter{Glosario de Términos y Herramientas Clásicas}

\\begin{description}
    \\item[Atributos Ext2 (chattr / lsattr):] Banderas extendidas del sistema de archivos Linux Ext2/Ext3 que permiten fijar políticas de inmutabilidad (\\texttt{+i}) o escritura append-only (\\texttt{+a}) a nivel del controlador de disco, inaccesibles a las llamadas estándar de permisos POSIX.
    \\item[Eggdrop:] Uno de los bots IRC más populares y longevos de la historia de Internet, creado originalmente en 1993 por Robey Pointer. Escrito en C y extensible mediante scripts en Tcl, solía ser empleado para mantener presencia en canales IRC.
    \\item[Grave-robber:] Herramienta modular de recolección de evidencia pericial perteneciente al paquete \\textit{The Coroner's Toolkit} (TCT), diseñada para recopilar información volátil y estática de un sistema Unix de manera forense.
    \\item[Inodo (Inode):] Estructura de datos fundamental en sistemas de archivos Unix que almacena todos los metadatos de un archivo (propietario, grupo, permisos, tamaño, marcas de tiempo y punteros a bloques de datos) excepto su nombre y el contenido mismo de los datos.
    \\item[mactime:] Utilidad de correlación temporal que toma la salida de herramientas de inspección de inodos (como \\texttt{ils} o \\texttt{fls}) y genera una línea de tiempo ordenada cronológicamente de todas las modificaciones, accesos y cambios en los metadatos de los archivos.
    \\item[psyBNC:] Servidor proxy / bouncer para IRC multiusuario que permite a los clientes ocultar su dirección IP real al conectarse a redes IRC y mantener conexiones persistentes aun cuando el cliente desconecte su equipo.
    \\item[Rootkit:] Conjunto de herramientas y binarios maliciosos diseñados para ocultar la presencia de un intruso y garantizar su acceso continuo con privilegios de administrador (\\texttt{root}) evadiendo los mecanismos ordinarios de detección del sistema operativo.
    \\item[SUID (Set User ID):] Bit de permiso especial en sistemas Unix que instruye al sistema operativo a ejecutar un programa con los privilegios del propietario del archivo (frecuentemente \\texttt{root}) en lugar de los privilegios del usuario que lo invoca.
    \\item[The Coroner's Toolkit (TCT):] Colección pionera de programas para análisis forense digital y respuesta a incidentes en sistemas Unix, concebida por Dan Farmer y Wietse Venema en 1999.
    \\item[The Sleuth Kit (TSK):] Biblioteca y conjunto de utilidades forenses de línea de comandos desarrollada por Brian Carrier como sucesora y evolución de TCT, base del entorno gráfico \\textit{Autopsy}.
    \\item[unrm:] Herramienta especializada en la recuperación de datos no asignados en sistemas de archivos Unix, capaz de examinar los bloques del disco marcados como libres y extraer su contenido antes de que sea sobreescrito.
\\end{description}
"""
with open(os.path.join(BASE_DIR, "appendices", "apendice_c_glosario.tex"), "w", encoding="utf-8") as f:
    f.write(apendice_c.strip() + "\n")
print("Created apendice_c_glosario.tex")

print("All chapters, appendices, and metadata generated successfully!")
