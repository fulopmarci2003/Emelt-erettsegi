def kerekit(n):
    if int(str(n)[-1]) in range(0, 3):
        return int(str(n)[:-1] + '0')
    if int(str(n)[-1]) in range(3, 8):
        return int(str(n)[:-1] + '5')
    if int(str(n)[-1]) in range(8, 10):
        return int(str(n)[:-1] + '0') + 10

#1, feladat
with open('eladott.txt', 'r', encoding='utf-8') as fin:
    max_jegy, vonal_hosz, ar = tuple(map(int, fin.readline().strip().split()))
    jegyek = []
    for sor in fin:
        jegyek.append(list(map(int, sor.strip().split())))

#2. feladat
print('2. feladat')
print(f'A legutolsó jegyvásárló ülésének sorszáma {jegyek[-1][0]} és az általa beutazott távolság {jegyek[-1][2] - jegyek[-1][1]} km')

#3. feladat
print('3. feladat')
for i, jegy in enumerate(jegyek, start=1):
    if jegy[1] == 0 and jegy[2] == vonal_hosz:
        print(i, end=' ')

#4. feladat
print('\n4. feladat')
bevetel = 0
for jegy in jegyek:
    bevetel += kerekit(((jegy[2] - jegy[1]) // 10 + 1) * ar)
print(f'A jegyekből {bevetel}-Ft bevétele származott a társaságnak!')

#5. feladat
print('5. feladat')
leszall_helyek = sorted(list({jegy[2] for jegy in jegyek}))
leszall = leszall_helyek[-2]
fel, le = 0, 0
for jegy in jegyek:
    if jegy[1] == leszall:
        fel += 1
    if jegy[2] == leszall:
        le += 1
print(f'Felszállók száma: {fel}\nLeszállók száma: {le}')

#6. feladat
print('6. feladat')
print(f'A leszállóhelyek száma: {len(leszall_helyek) - 2}')

#7. feladat
beker = int(input('Adjon meg egy km állást!'))
with open('kihol.txt', 'w', encoding='utf-8') as fout:
    ulesek_by_km = []
    for hely in range(1, max(list(zip(*jegyek))[0]) + 1):
        for index, jegy in enumerate(jegyek, start=1):
            if jegy[0] == hely and jegy[1] < beker <= jegy[2]:
                ulesek_by_km.append([jegy[0], f'{index}. utas'])
    for hely in range(1, max(list(zip(*jegyek))[0]) + 1):
        if hely not in list(zip(*ulesek_by_km))[0]:
            ulesek_by_km.append([hely, 'Üres'])
    for data in sorted(ulesek_by_km):
        fout.write(f'{data[0]}. ülés: {data[1]}\n')






