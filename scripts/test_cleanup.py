import re

def convert_spanish_accents(text):
    # Mapping of babel activeacute and ancient TeX accents to clean UTF-8
    # Only run outside \verb and \begin{verbatim} ... \end{verbatim}
    
    # First, handle explicit LaTeX accents
    replacements = [
        (r"\\'a", "á"), (r"\\'e", "é"), (r"\\'i", "í"), (r"\\'o", "ó"), (r"\\'u", "ú"),
        (r"\\'A", "Á"), (r"\\'E", "É"), (r"\\'I", "Í"), (r"\\'O", "Ó"), (r"\\'U", "Ú"),
        (r"\\~n", "ñ"), (r"\\~N", "Ñ"),
        (r'\\"u', "ü"), (r'\\"U', "Ü"),
        # activeacute: 'a -> á, etc.
        (r"'a", "á"), (r"'e", "é"), (r"'i", "í"), (r"'o", "ó"), (r"'u", "ú"),
        (r"'A", "Á"), (r"'E", "É"), (r"'I", "Í"), (r"'O", "Ó"), (r"'U", "Ú"),
        (r"~n", "ñ"), (r"~N", "Ñ"),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    return text

def modernize_latex_commands(text):
    # Convert obsolete font commands
    # {\bf foo} -> \textbf{foo}
    # {\em foo} -> \emph{foo}
    # {\it foo} -> \textit{foo}
    # {\tt foo} -> \texttt{foo}
    text = re.sub(r"\{\\bf\s+([^}]+)\}", r"\\textbf{\1}", text)
    text = re.sub(r"\{\\em\s+([^}]+)\}", r"\\emph{\1}", text)
    text = re.sub(r"\{\\it\s+([^}]+)\}", r"\\textit{\1}", text)
    text = re.sub(r"\{\\tt\s+([^}]+)\}", r"\\texttt{\1}", text)
    text = re.sub(r"\{\\footnotesize\s+([^}]+)\}", r"{\\footnotesize \1}", text)
    # Convert \verb+foo+ to \texttt{foo} when safe or keep \verb
    # Clean up ASCII dash lines like \centerline {-----------------------------}
    text = re.sub(r"\\centerline\s*\{[-—_]{5,}\}", r"\\hrulefill\\medskip", text)
    text = re.sub(r"[-—_]{20,}", r"\\hrulefill", text)
    return text

print("Testing...")
sample = "El an'alisis forense permiti'o verificar que la m'aquina ten'ia {\bf rootkits} y no un virus com'un."
print("Before:", sample)
print("After :", modernize_latex_commands(convert_spanish_accents(sample)))
