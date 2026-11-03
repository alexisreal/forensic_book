import glob
import re

tex_files = [p for p in glob.glob("/Users/alexis/work/reporte-forense/**/*.tex", recursive=True) if "original" not in p]

errors = []
for path in sorted(tex_files):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # check open/close environments
    begins = re.findall(r"\\begin\{([a-zA-Z*]+)\}", content)
    ends = re.findall(r"\\end\{([a-zA-Z*]+)\}", content)
    
    from collections import Counter
    b_count = Counter(begins)
    e_count = Counter(ends)
    
    for env in set(list(b_count.keys()) + list(e_count.keys())):
        if b_count[env] != e_count[env]:
            errors.append(f"{path}: environment '{env}' mismatch: {b_count[env]} begins, {e_count[env]} ends")

if not errors:
    print(f"All {len(tex_files)} generated TeX files are valid UTF-8 and have balanced environments!")
else:
    for err in errors:
        print("ERROR:", err)
