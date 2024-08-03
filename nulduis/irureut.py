import ipaddress

def merge_cids(cidr1, cidr2):
    network1 = ipaddress.ip_network(cidr1)
    network2 = ipaddress.ip_network(cidr2)

    if network1.overlaps(network2):
        start = max(network1.network_address, network2.network_address)
        end = min(network1.broadcast_address, network2.broadcast_address)
        return str(ipaddress.ip_network(f"{start}/{min(network1.prefixlen, network2.prefixlen)}"))
    else:
        return [str(cidr1), str(cidr2)]

cidr1 = "192.0.2.0/24"
cidr2 = "192.0.2.128/25"

print(merge_cids(cidr1, cidr2))  # Output: 192.0.2.0/24
