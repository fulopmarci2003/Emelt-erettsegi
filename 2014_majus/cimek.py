with open('ip.txt', 'r', encoding='utf-8') as in_file:
    list_ipadresses = []
    file = in_file.readline()[0:-1]
    while file:
        list_ipadresses.append(file)
        file = in_file.readline()[0:-1]

print(f'2. feladat\nAz állományban {len(list_ipadresses)} darab adatsor van.')
print(f'\n3. feladat:\nA legalacsonyabb tárolt IP-cím:\n{sorted(list_ipadresses)[0]}')
print('\n4.feladat')
a, b, c = 0, 0, 0
for ip in list_ipadresses:
    if ip.startswith('2001:0db8'):
        a += 1
    if ip.startswith('2001:0e'):
        b += 1
    if ip.startswith('fc') or ip.startswith('fd'):
        c += 1
print(f'Dokumentációs cím: {a} darab\nGlobális egyedi cím: {b} darab\nHelyi egyedi cím: {c} darab')
with open('sok.txt', 'w') as out_file:
    for i, ip in enumerate(list_ipadresses, start=1):
        if ip.count('0') >= 18:
            out_file.write(f'{i} {ip}\n')
line = int(input("adj meg egy sort"))
list_ip = list_ipadresses[line - 1].split(':')
for i in range(len(list_ip)):
    if list_ip[i] == '0000':
        list_ip[i] = 0
        continue
    while list_ip[i].startswith('0'):
         list_ip[i] = list_ip[i][1:]
print(*list_ip, sep=':')

