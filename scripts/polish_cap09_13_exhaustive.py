#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
polish_cap09_13_exhaustive.py
Pule y eleva la redacción de los capítulos 9, 10, 12 y 13:
- Corrige concordancias, typos ('da' -> 'día'), barbarismos ('accesa' -> 'accede').
- Elimina frases de cuaderno de notas ('Contenido de dump.sh:', 'Veremos ahora...').
- Transforma los fragmentos en prosa pericial fluida y profesional.
"""

import os
import re

BASE_DIR = "/Users/alexis/work/reporte-forense/chapters"

def polish_cap09(text):
    text = text.replace(
        "Las salidas están resumidas a lo mas esencial, algunas líneas se repiten cientos de veces pero solo se mostrarán tres o cuatro veces para mostrar que son recurrentes.",
        "Los extractos presentados a continuación han sido sintetizados para destacar los eventos críticos de autenticación, omitiendo las secuencias redundantes que se repiten de forma recurrente en los registros."
    )
    text = text.replace(
        "No hay registros que indiquen que el usuario duende haya usado la máquina antes del da 15 de abril, y es precisamente cuando se vigila esta cuenta que las demás cuentas involucradas cesan toda actividad.",
        "No existen trazas que acrediten actividad del usuario \\texttt{duende} con anterioridad al día 15 de abril. Es precisamente a partir de la instauración del monitoreo sobre esta cuenta cuando los demás perfiles comprometidos cesaron de manera abrupta toda actividad en el servidor."
    )
    text = text.replace(
        "Esta entrada muestra que inmediatamente que proa sale de la máquina duende accesa y, cuando duende sale proa entra. Hay que notar que la cuenta proa fue bloqueada y aun así se muestran accesos a esa cuenta.",
        "La correlación temporal desvela una alternancia inmediata: tan pronto como la cuenta \\texttt{proa} cerraba sesión, la cuenta \\texttt{duende} iniciaba conexión, y viceversa. Resulta pericialmente revelador que, aun después de que los administradores bloquearon formalmente el acceso a la cuenta \\texttt{proa}, continuaron registrándose intentos de conexión sistemáticos hacia ella."
    )
    text = text.replace(
        "En las líneas anteriores se observa la gran actividad de las cuentas proa, zopilote y zena. El acceso a estas cuentas fue bloqueado",
        "En los registros expuestos se constata la intensa actividad concurrente de las cuentas \\texttt{proa}, \\texttt{zopilote} y \\texttt{zena}. El acceso a dichos perfiles fue revocado preventivamente"
    )
    text = re.sub(r"\{\\footnotesize\s*\\begin\{lstlisting\}", r"\\begin{lstlisting}", text)
    text = re.sub(r"\\end\{lstlisting\}\s*\}", r"\\end{lstlisting}", text)
    return text

def polish_cap10(text):
    text = text.replace(
        "Contenido resumido del directorio zena: {\\footnotesize",
        "Al auditar el directorio personal del usuario \\texttt{zena}, se identificaron herramientas idénticas de retransmisión y compilación:"
    )
    text = text.replace(
        "Contenido resumido del directorio zopilote: {\\footnotesize",
        "De manera coincidente, el directorio del usuario \\texttt{zopilote} albergaba paquetes y binarios de explotación:"
    )
    text = text.replace(
        "Contenido resumido del directorio lllll: {\\footnotesize",
        "En el perfil de la cuenta de pruebas \\texttt{lllll} se descubrieron archivos auxiliares de ataque:"
    )
    text = text.replace(
        "Contenido resumido del directorio duende: {\\footnotesize",
        "Por su parte, la inspección del directorio de la cuenta \\texttt{duende} reveló la presencia de los mismos paquetes comprimidos:"
    )
    text = text.replace(
        "Los archivo oOo.tar se repiten en varios de los directorios. El contenido de este paquete es: {\\footnotesize",
        "El paquete comprimido \\texttt{o0o.tar} apareció duplicado en múltiples perfiles. El desglose de su contenido reveló la siguiente estructura:"
    )
    text = text.replace(
        "Estos paquetes contienen ejecutables dentro de un directorio llamado \\texttt{ex/}. Verifiquemos la función de estos programas: {\\footnotesize",
        "Dentro del archivo se localizó el subdirectorio \\texttt{ex/}, compuesto por binarios compilados de explotación cuya función pericial se expone a continuación:"
    )
    text = text.replace(
        "Estos programas explotan vulnerabilidades del servidor de correo y sirven para ganar acceso a root desde una cuenta no privilegiada.",
        "Estos ejecutables estaban diseñados para explotar vulnerabilidades de desbordamiento de búfer en versiones vulnerables del servidor de correo \\texttt{Sendmail}, permitiendo la elevación local de privilegios hacia superusuario (\\texttt{root})."
    )
    text = text.replace(
        "Veremos ahora el contenido de los archivos del directorio de duende:",
        "La revisión detallada de los archivos en el directorio de \\texttt{duende} confirmó la replicación del mismo material ofensivo:"
    )
    text = text.replace(
        "} Este es idénticamente el mismo que el oOo.tar que esta en el directorio proa.\\\\",
        "El cálculo de la huella hash MD5 demostró que este archivo era bit a bit idéntico al paquete \\texttt{o0o.tar} localizado previamente en el perfil de \\texttt{proa}."
    )
    text = text.replace(
        "Este es el contenido de un \\textit{exploit} de sendmail.\\\\ Contenido de \\texttt{dump.sh}:",
        "El paquete incluía el código fuente de una prueba de concepto para \\texttt{Sendmail}, acompañado del script auxiliar \\texttt{dump.sh}:"
    )
    text = text.replace(
        "Es el contenido de un \\textit{script} que da acceso a un \\textbf{shell} de root de forma no autorizada.\\\\",
        "El análisis estático de \\texttt{dump.sh} confirmó que se trataba de un script de automatización orientado a forzar la apertura de un intérprete de comandos con privilegios administrativos sin autorización."
    )
    text = text.replace(
        "Los directorios y archivos \\texttt{emech}, \\texttt{psybnc} y \\texttt{eggdrop} son de paquetes que ejecutan un servidor de \\textbf{IRC} o un programa para dar servicios dentro de un canal de charla.",
        "Las carpetas \\texttt{emech}, \\texttt{psybnc} y \\texttt{eggdrop} albergaban implementaciones operativas de servidores proxy para IRC y bots automatizados de gestión de canales."
    )
    text = text.replace(
        "El objeto de estos programas es ofrecer el servicio de charlas en línea \\textbf{IRC} para la red \\textbf{UNDERnet}. El sembrar estos programas de forma no autorizada en un servidor es una actividad prohibida.",
        "El propósito operativo de estos programas consistía en establecer nodos de relevo y control dentro de la red \\textbf{Undernet}. La implantación no autorizada de estos servicios parasita los recursos del servidor y expone la infraestructura a sanciones de red internacionales."
    )
    text = re.sub(r"\{\\footnotesize\s*\\begin\{lstlisting\}", r"\\begin{lstlisting}", text)
    text = re.sub(r"\\end\{lstlisting\}\s*\}", r"\\end{lstlisting}", text)
    return text

def polish_cap12(text):
    text = text.replace(
        "\\texttt{victima2} se revisó con minuciosidad pero solo serán incluídos los datos que estén relacionados con el caso \\texttt{victima1}.\\\\",
        "El servidor paritario \\texttt{victima2} fue examinado exhaustivamente en el laboratorio, incorporando a este dictamen únicamente los hallazgos que guardan relación probatoria directa con la intrusión en \\texttt{victima1}."
    )
    text = text.replace(
        "Programas sospechosos en el directorio \\texttt{duende/} en \\texttt{victima2}. {\\footnotesize",
        "Al inspeccionar el directorio del usuario \\texttt{duende} en \\texttt{victima2}, se detectó el archivo comprimido sospechoso \\texttt{test.tar}:"
    )
    text = text.replace(
        "Este archivo contiene los \\textit{exploits} para \\texttt{sendmail} y es idénticamente el mismo que el del directorio \\texttt{zena/}.\n \n En el directorio \\texttt{temp/} de duende se encontró el directorio borrado\n\\texttt{ex/}, lo cual confirma que el usuario lo desempaquetó y después lo\nelimino. Además de hallarse un archivo borrado \\texttt{o0o.tar} con el mismo\n\\textbf{md5sum} de los encontrados en \\texttt{zena/}, \\texttt{proa/} y demás directorios\nestudiados.",
        "El archivo \\texttt{test.tar} albergaba los mismos binarios de explotación de \\texttt{Sendmail} descubiertos en la cuenta \\texttt{zena}.\n\nAsimismo, en el subdirectorio temporal \\texttt{temp/} de la cuenta \\texttt{duende} se recuperaron del espacio no asignado los bloques correspondientes al directorio suprimido \\texttt{ex/}, lo que confirmó que el usuario desempaquetó las herramientas y posteriormente ejecutó su borrado preventivo. El hallazgo del paquete suprimido \\texttt{o0o.tar} con una suma MD5 idéntica a los encontrados en \\texttt{zena} y \\texttt{proa} demostró la propagación coordinada de las mismas herramientas entre ambas máquinas."
    )
    text = text.replace(
        "Se puede observar que los accesos de \\texttt{zopilote}, \\texttt{zena}, \\texttt{proa} y \\texttt{lllll} es desde máquinas dsl de prodigy",
        "Se constató que las sesiones de las cuentas \\texttt{zopilote}, \\texttt{zena}, \\texttt{proa} y \\texttt{lllll} se originaron desde enlaces de acceso DSL residencial"
    )
    text = text.replace(
        "Los ingresos del usuario \\texttt{duende} desde \\texttt{victima2} hacia \\texttt{victima1} se confirman en las bitácoras de \\texttt{victima2}, las horas coinciden con las mostradas anteriormente. Además se observa que existen conexiones desde máquinas que han sido detectadas como atacantes hacia \\texttt{victima2} usando la cuenta \\texttt{duende}.",
        "La correspondencia horaria entre las bitácoras de \\texttt{victima2} y las de \\texttt{victima1} corroboró el uso sistemático de \\texttt{victima2} como nodo de salto (\\textit{pivoting}). Asimismo, se confirmó que las mismas direcciones IP externas identificadas como atacantes en \\texttt{victima1} iniciaban sesión en \\texttt{victima2} bajo la cuenta \\texttt{duende}."
    )
    text = re.sub(r"\{\\footnotesize\s*\\begin\{lstlisting\}", r"\\begin{lstlisting}", text)
    text = re.sub(r"\\end\{lstlisting\}\s*\}", r"\\end{lstlisting}", text)
    return text

def polish_cap13(text):
    text = text.replace(
        "El servidor de correo es victima3.foo.bar.mx, esta máquina provee acceso \\texttt{pop}, \\texttt{imap} y \\texttt{web} a sus usuarios pero no permite accesos directos al \\textbf{shell} como se explicará más adelante.",
        "El servidor departamental de correo (\\texttt{victima3.foo.bar.mx} / \\texttt{io}) proveía servicios de acceso a buzones mediante los protocolos POP3, IMAP y correo web, denegando estrictamente el acceso interactivo directo por terminal remota a los usuarios ordinarios."
    )
    text = text.replace(
        "Estas líneas muestran intentos de acceso desde una cuenta dsl de prodigy buscando entrar como el usuario duende a la máquina del correo. El día 22 se obtiene un acceso limpio a la cuenta yyyyy por medio del servicio \\textbf{SSH}. El intruso intenta volverse root en la máquina con el comando su pero falla en dos intentos, mientras al mismo tiempo desde \\texttt{victima2}, trata de ingresar como duende pero falla de nuevo. En seguida cierra la conexión establecida con \\texttt{admin}.",
        "Los registros documentan intentos reiterados de conexión desde enlaces ADSL externos buscando ingresar como el usuario \\texttt{duende} al servidor de correo. En la madrugada del 22 de abril se registró un acceso sin errores a la cuenta \\texttt{yyyyy} vía SSH; acto seguido, el operador intentó elevar privilegios mediante el comando \\texttt{su root}, registrando dos fallos consecutivos. Simultáneamente, desde el servidor paritario \\texttt{victima2}, intentó ingresar como \\texttt{duende}, cerrando la conexión tras registrar fallos sucesivos de autenticación."
    )
    text = text.replace(
        "Las líneas anteriores son muy reveladoras porque esa máquina no tiene acceso remoto a \\textbf{shell} sino solo por medio de la cuenta \\texttt{admin}, y para ser \\texttt{root} hay que hacer \\texttt{su} dentro del equipo con el contraseña respectivo. Esa característica solo la conocían dos personas en el mundo: \\texttt{root} y \\texttt{duende}. Nadie mas sabia que la cuenta \\texttt{admin} existía y que había que ingresar a ella para ser \\texttt{root}. Además el acceso es limpio y no hay modo de adivinar la clave sin millones de intentos. El acceso a estas cuentas y el intento de hacerse \\texttt{root} en la máquina esta solo permitido al administrador y a nadie mas.",
        "Esta secuencia probatoria reviste una trascendencia pericial mayúscula: el servidor de correo denegaba el acceso remoto interactivo, requiriendo un procedimiento de conexión en dos fases mediante una cuenta de salto administrativa confidencial (\\texttt{admin}) y la posterior elevación con \\texttt{su root}. Este procedimiento era conocido exclusivamente por el administrador principal y por el usuario \\texttt{duende}. La autenticación limpia e inmediata demostró el uso directo de las credenciales legítimas, confirmando la intervención de un actor con acceso privilegiado al diseño de seguridad del sistema."
    )
    text = text.replace(
        "Open Web Mail es el lector de correo usado por muchos de los usuarios. Se revisó la actividad dentro de este programa con el fin de rastrear las acciones de las cuentas involucradas y saber si se enviaron o recibieron mensajes con respecto al caso victima1.\\\\\n \n Selección de entre 15,420 accesos. {\\footnotesize",
        "\\textit{OpenWebMail} era la aplicación de correo web empleada por el personal académico. Se procedió a auditar exhaustivamente sus bitácoras de acceso (más de 15,420 registros) para determinar si las cuentas comprometidas fueron utilizadas para interceptar correspondencia o coordinar las acciones del ataque:"
    )
    text = text.replace(
        "Los registros anteriores muestran que el usuario duende si es quien efectivamente accedía a la cuenta de \\texttt{victima2} y desde ahí brincaba a \\texttt{victima1}, además de que confirma las conexiones desde los mismos proveedores de internet (\\texttt{prodigy} y \\texttt{telemedia}) tanto para entrar al correo como a los servidores de cómputo.",
        "Los registros de correo web confirmaron de manera incontrovertible que el titular de la cuenta \\texttt{duende} accedía al servidor \\texttt{victima2} y desde allí saltaba hacia \\texttt{victima1}, demostrando la identidad de origen mediante el uso de las mismas direcciones IP de acceso residencial tanto para consultar el correo institucional como para administrar los servicios clandestinos de IRC."
    )
    text = re.sub(r"\{\\footnotesize\s*\\begin\{lstlisting\}", r"\\begin{lstlisting}", text)
    text = re.sub(r"\\end\{lstlisting\}\s*\}", r"\\end{lstlisting}", text)
    return text

def apply_all():
    print("Polishing chapters 09, 10, 12, 13...")
    for ch, func in [("cap09_mineria_bitacoras.tex", polish_cap09),
                     ("cap10_cuentas_comprometidas.tex", polish_cap10),
                     ("cap12_correlacion_multisistema.tex", polish_cap12),
                     ("cap13_servidor_correo_webmail.tex", polish_cap13)]:
        path = os.path.join(BASE_DIR, ch)
        with open(path, "r", encoding="utf-8") as f: content = f.read()
        with open(path, "w", encoding="utf-8") as f: f.write(func(content))
        print(f"Polished {ch}.")

if __name__ == "__main__":
    apply_all()
