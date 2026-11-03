import re
from collections import defaultdict

with open("/Users/alexis/work/reporte-forense/original/reporte-publico-original.tex", "r", encoding="latin1") as f:
    text = f.read()

# Find all IP addresses
ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
ips = ip_pattern.findall(text)

counts = defaultdict(int)
for ip in ips:
    counts[ip] += 1

print(f"Total IP occurrences: {len(ips)}")
print(f"Unique IPs: {len(counts)}")

subnets = defaultdict(list)
for ip, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    parts = ip.split(".")
    subnet = ".".join(parts[:3])
    subnets[subnet].append((ip, count))

print(f"Total /24 subnets: {len(subnets)}")
for subnet, ip_list in sorted(subnets.items(), key=lambda x: len(x[1]), reverse=True)[:15]:
    print(f"Subnet {subnet}.x: {len(ip_list)} unique IPs, total {sum(c for _, c in ip_list)} occurrences")
    for ip, c in ip_list[:3]:
        print(f"   {ip} (x{c})")
