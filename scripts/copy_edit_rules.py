import re

# Comprehensive list of regex substitutions for copy-editing (Spanish orthography & technical grammar)
# Applied ONLY to prose outside \begin{lstlisting} ... \end{lstlisting}

TEXT_REPLACEMENTS = [
    # Barbarisms and anglicisms
    (r"\baccesaba\b", "accedía"),
    (r"\baccesaban\b", "accedían"),
    (r"\baccesar\b", "acceder"),
    (r"\baccesó\b", "accedió"),
    (r"\bacceso a\b", "acceso a"), # preserve noun
    (r"\bchecar\b", "verificar"),
    (r"\bchecó\b", "verificó"),
    (r"\bchecaron\b", "verificaron"),
    (r"\bchequeo\b", "verificación"),
    (r"\bpassword\b", "contraseña"),
    (r"\bpasswords\b", "contraseñas"),
    (r"\bPassword\b", "Contraseña"),
    (r"\bPasswords\b", "Contraseñas"),
    
    # Missing verb accents (past / future)
    (r"\bse revisara\b", "se revisará"),
    (r"\bse estudiaran\b", "se estudiarán"),
    (r"\bse mostraran\b", "se mostrarán"),
    (r"\bse explicara\b", "se explicará"),
    (r"\bse encontraran\b", "se encontrarán"),
    (r"\bse incluiran\b", "se incluirán"),
    (r"\bse recuperara\b", "se recuperará"),
    (r"\bse trabajo\b", "se trabajó"),
    (r"\bse realizo\b", "se realizó"),
    (r"\bse analizo\b", "se analizó"),
    (r"\bse encontro\b", "se encontró"),
    (r"\bse procedio\b", "se procedió"),
    (r"\bse recupero\b", "se recuperó"),
    (r"\bse detecto\b", "se detectó"),
    (r"\bse observo\b", "se observó"),
    (r"\bse confirmo\b", "se confirmó"),
    (r"\bse verifico\b", "se verificó"),
    (r"\bse ejecuto\b", "se ejecutó"),
    (r"\bse instalo\b", "se instaló"),
    (r"\bse descubrio\b", "se descubrió"),
    (r"\bse inicio\b", "se inició"),
    (r"\bse trato\b", "se trató"),
    (r"\bse borro\b", "se borró"),
    (r"\bse creo\b", "se creó"),
    
    # General words missing accents
    (r"\bdió\b", "dio"), # RAE: monosyllables have no accent
    (r"\bvió\b", "vio"),
    (r"\bfué\b", "fue"),
    (r"\btambien\b", "también"),
    (r"\bademas\b", "además"),
    (r"\bdespues\b", "después"),
    (r"\bningun\b", "ningún"),
    (r"\bninguna\b", "ninguna"),
    (r"\balgun\b", "algún"),
    (r"\balguna\b", "alguna"),
    (r"\bsegun\b", "según"),
    (r"\blinea\b", "línea"),
    (r"\blineas\b", "líneas"),
    (r"\bmaquina\b", "máquina"),
    (r"\bmaquinas\b", "máquinas"),
    (r"\bbitacora\b", "bitácora"),
    (r"\bbitacoras\b", "bitácoras"),
    (r"\bcodigo\b", "código"),
    (r"\bcodigos\b", "códigos"),
    (r"\bnumero\b", "número"),
    (r"\bnumeros\b", "números"),
    (r"\bperiodo\b", "período"),
    (r"\bultimo\b", "último"),
    (r"\bultima\b", "última"),
    (r"\bultimos\b", "últimos"),
    (r"\bultimas\b", "últimas"),
    (r"\bproposito\b", "propósito"),
    (r"\bpropositos\b", "propósitos"),
    (r"\bmetodo\b", "método"),
    (r"\bmetodos\b", "métodos"),
    (r"\btactica\b", "táctica"),
    (r"\btacticas\b", "tácticas"),
    (r"\btecnica\b", "técnica"),
    (r"\btecnicas\b", "técnicas"),
    (r"\barbol\b", "árbol"),
    (r"\barboles\b", "árboles"),
    (r"\bexito\b", "éxito"),
    (r"\bcomun\b", "común"),
    (r"\bcomunes\b", "comunes"),
    (r"\bunicamente\b", "únicamente"),
    (r"\bunico\b", "único"),
    (r"\bunica\b", "única"),
    (r"\bunicos\b", "únicos"),
    (r"\bunicas\b", "únicas"),
    (r"\bmas como\b", "pero como"),
    (r"\bmas no\b", "pero no"),
    
    # False accents
    (r"\bFunciónes\b", "Funciones"),
    (r"\bfunciónes\b", "funciones"),
    (r"\bimágenes\b", "imágenes"),
    (r"\borígenes\b", "orígenes"),
    
    # Ortotypography of foreign words
    (r"\brootkits\b", r"\\textit{rootkits}"),
    (r"\brootkit\b", r"\\textit{rootkit}"),
    (r"\bRootkits\b", r"\\textit{Rootkits}"),
    (r"\bRootkit\b", r"\\textit{Rootkit}"),
    (r"\bsniffers\b", r"\\textit{sniffers}"),
    (r"\bsniffer\b", r"\\textit{sniffer}"),
    (r"\bexploits\b", r"\\textit{exploits}"),
    (r"\bexploit\b", r"\\textit{exploit}"),
    (r"\bbackdoors\b", r"\\textit{backdoors}"),
    (r"\bbackdoor\b", r"\\textit{backdoor}"),
    (r"\bbouncers\b", r"\\textit{bouncers}"),
    (r"\bbouncer\b", r"\\textit{bouncer}"),
    (r"\bcracking\b", r"\\textit{cracking}"),
    (r"\bcrackers\b", r"\\textit{crackers}"),
    (r"\bcracker\b", r"\\textit{cracker}"),
    (r"\bmalware\b", r"\\textit{malware}"),
    (r"\bscripts\b", r"\\textit{scripts}"),
    (r"\bscript\b", r"\\textit{script}"),
    
    # Capitalization & technical standards
    (r"\bIp\b", "IP"),
    (r"\bips\b", "IPs"),
    (r"\bssh\b", "SSH"),
    (r"\bftp\b", "FTP"),
    (r"\bsamba\b", "Samba"),
    (r"\bnfs\b", "NFS"),
    (r"\birc\b", "IRC"),
    (r"\blinux\b", "Linux"),
]

def apply_copy_editing_to_prose(text):
    for pattern, repl in TEXT_REPLACEMENTS:
        text = re.sub(pattern, repl, text)
    
    # Clean \verb+...+ to \texttt{...}
    text = re.sub(r"\\verb\+([^+]+)\+", r"\\texttt{\1}", text)
    
    # Clean raw \begin{alltt} ... \end{alltt}
    text = text.replace(r"\begin{alltt}", r"\begin{lstlisting}[style=terminal]")
    text = text.replace(r"\end{alltt}", r"\end{lstlisting}")
    
    # Clean stray {\footnotesize surrounding listings
    text = re.sub(r"\{\\footnotesize\s*\\begin\{lstlisting\}", r"\\begin{lstlisting}", text)
    text = re.sub(r"\\end\{lstlisting\}\s*\}", r"\\end{lstlisting}", text)
    
    # Clean line-breaking \\ in prose (where followed by a newline and word)
    text = re.sub(r"\\\\(?:\s*[\r\n]+)(?=[A-ZÁÉÍÓÚa-záéíóú\\])", "\n\n", text)
    
    # Clean consecutive spaces
    text = re.sub(r"[ \t]{2,}", " ", text)
    
    return text

print("Rules defined.")
