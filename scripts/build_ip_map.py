import re

# RFC 5737 and private IP pools for anonymization
# We want to map each unique /24 subnet to an RFC 5737 subnet:
# TEST-NET-1: 192.0.2.0/24
# TEST-NET-2: 198.51.100.0/24
# TEST-NET-3: 203.0.113.0/24
# Documentation IPv4 blocks:
# 192.0.2.x, 198.51.100.x, 203.0.113.x, plus private blocks like 10.10.x.x, 172.16.x.x, etc.

def build_ip_anonymizer(text):
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    all_ips = set(ip_pattern.findall(text))
    
    # Do not anonymize loopback 127.0.0.1 or broadcast
    exempt = {"127.0.0.1", "0.0.0.0", "255.255.255.255"}
    target_ips = [ip for ip in all_ips if ip not in exempt]
    
    # Group by /24
    subnets = {}
    for ip in target_ips:
        prefix = ".".join(ip.split(".")[:3])
        if prefix not in subnets:
            subnets[prefix] = []
        subnets[prefix].append(ip)
    
    # Sort subnets by frequency in text
    subnet_counts = {p: sum(text.count(ip) for ip in ips) for p, ips in subnets.items()}
    sorted_subnets = sorted(subnets.keys(), key=lambda p: subnet_counts[p], reverse=True)
    
    # Allocate fake subnets:
    # 200.78.118 (top attacker pool) -> 198.51.100.x
    # 200.67.75 (second pool) -> 203.0.113.x
    # 200.77.149 -> 192.0.2.x
    # others -> 198.18.x.x, 198.19.x.x (benchmarking RFC 2544) or 10.x.x.x
    subnet_map = {}
    
    base_subnets = [
        "198.51.100",  # TEST-NET-2
        "203.0.113",   # TEST-NET-3
        "192.0.2",     # TEST-NET-1
    ]
    # Add 198.18.1 through 198.18.60 for the rest
    for i in range(1, 100):
        base_subnets.append(f"198.18.{i}")
        
    for idx, real_subnet in enumerate(sorted_subnets):
        fake_subnet = base_subnets[idx]
        subnet_map[real_subnet] = fake_subnet
        
    ip_map = {}
    for ip in target_ips:
        parts = ip.split(".")
        real_prefix = ".".join(parts[:3])
        last_octet = parts[3]
        fake_prefix = subnet_map[real_prefix]
        ip_map[ip] = f"{fake_prefix}.{last_octet}"
        
    return ip_map

if __name__ == "__main__":
    with open("/Users/alexis/work/reporte-forense/original/reporte-publico-original.tex", "r", encoding="latin1") as f:
        text = f.read()
    ip_map = build_ip_anonymizer(text)
    print(f"Mapped {len(ip_map)} IPs to RFC 5737/2544 test ranges.")
    for real in list(ip_map.keys())[:10]:
        print(f"  {real} -> {ip_map[real]}")
