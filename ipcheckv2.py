hosts = {
    '192.168.1.1': [22, 80, 443],
    '192.168.1.2': [3389, 445],
    '10.0.0.1': [22],
    # TODO: dopisz 2 nowe hosty:
    '10.0.0.2': [587, 3389],
    '10.0.0.3': [20, 21, 22, 80]
}

rdp_port = 3389
# Twoja wersja (działa):

rdp_count = 0
# Nowa wersja (jedna linijka):
rdp_count = sum(1 for ports in hosts.values() for p in ports if p == rdp_port)
print("Liczba wystąpień portu 3389:", rdp_count)
