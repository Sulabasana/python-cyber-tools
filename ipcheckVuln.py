def find_vuln_ports(hosts, port_list):
    """
    Zwraca słownik: host -> lista niebezpiecznych portów z port_list.
    Np. {'192.168.1.2': [3389, 445]}
    """
    result = {}
    for host, ports in hosts.items():
        vuln_on_host = [p for p in ports if p in port_list]
        if vuln_on_host:  # tylko hosty z vuln portami
            result[host] = vuln_on_host
    return result

# Twoje dane testowe
hosts = {
    '192.168.1.1': [22, 80, 443],
    '192.168.1.2': [3389, 445],
    '10.0.0.1': [22],
    '10.0.0.2': [587, 3389],
    '10.0.0.3': [20, 21, 22, 80]
}

vuln_ports = [445, 3389, 23]  # RDP, SMB, Telnet

# Użyj funkcji!
vuln_hosts = find_vuln_ports(hosts, vuln_ports)
print("Hosty z vuln portami:", vuln_hosts)
# Wynik: {'192.168.1.2': [3389, 445], '10.0.0.2': [3389]}

# Test 1: tylko RDP
rdp_only = find_vuln_ports(hosts, [3389])
print("Tylko RDP:", rdp_only)

# Test 2: nowe porty
critical = [21, 23, 445]
print("Critical:", find_vuln_ports(hosts, critical))
