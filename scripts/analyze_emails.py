import re

with open("/Users/alexis/work/reporte-forense/original/reporte-publico-original.tex", "r", encoding="latin1") as f:
    text = f.read()

# email regex
emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text))
print(f"Total unique emails: {len(emails)}")

# categorize emails
domains = set()
for e in sorted(emails):
    user, dom = e.split("@", 1)
    domains.add(dom.lower())

print(f"Domains ({len(domains)}):")
for d in sorted(domains):
    print("  ", d)
