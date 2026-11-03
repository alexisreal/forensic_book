import re

with open("/Users/alexis/work/reporte-forense/original/reporte-publico-original.tex", "r", encoding="latin1") as f:
    text = f.read()

print("Matches for 'a:", len(re.findall(r"'a", text)))
print(r"Matches for \'a:", len(re.findall(r"\\'a", text)))
print("Matches for direct á:", len(re.findall(r"á", text)))
print("Matches for 'e:", len(re.findall(r"'e", text)))
print("Matches for 'i:", len(re.findall(r"'i", text)))
print("Matches for 'o:", len(re.findall(r"'o", text)))
print("Matches for 'u:", len(re.findall(r"'u", text)))
print("Matches for ñ:", len(re.findall(r"ñ", text)))
print(r"Matches for \~n:", len(re.findall(r"\\~n", text)))
print(r"Matches for ~n:", len(re.findall(r"~n", text)))
