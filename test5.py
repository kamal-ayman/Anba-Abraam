import socket as sc

print(sc.gethostname())
print(sc.gethostbyname('oliver'))
print(sc.getservbyname('ssh'))
print(sc.getservbyport(443))

