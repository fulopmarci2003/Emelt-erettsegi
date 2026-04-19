with open('szoveg.txt', 'r', encoding='utf-8') as fin:
    szavak = fin.read().strip().split('\n')

#1. feladat
print('1. feladat')
szo = input('Adjon meg egy szót: ')
if any(betu in ['a', 'e', 'i', 'o', 'u'] for betu in list(szo)):
    print('Van benne magánhangzó.')
else:
    print('Nincs benne magánhangzó.')

#2. feladat
print('2.feladat')
print(f'A leghosszabb szó a(z) "{max(szavak, key=len)}" és {len(max(szavak, key=len))} karakterből áll.')

#3. feladat
print('3.feladat')
sum_maganh = 0
for szo in szavak:
    maganh = len([word for word in list(szo) if word in ['a', 'e', 'i', 'o', 'u']])
    massalh = len([word for word in list(szo) if word not in ['a', 'e', 'i', 'o', 'u']])
    if maganh > massalh:
        sum_maganh += 1
print(f'{sum_maganh}/{len(szavak)} : {(sum_maganh/len(szavak)) * 100:.2f}%')

#4. feladat
print('4.feladat')
szavak_5 = []
for szo in szavak:
    if len(szo) == 5:
        szavak_5.append(szo)
szo_3 = input('Adj meg egy 3 betűből álló szórészletet!')
for szo in szavak_5:
    if szo[1:-1] == szo_3:
        print(szo, end=' ')

#5. feladat
szavak_3 = set()
for szo in szavak_5:
    szavak_3.add(szo[1:-1])
with open('letra.txt', 'w', encoding='utf-8') as fout:
    for szo_3 in szavak_3:
        words = []
        for szo_5 in szavak_5:
            if szo_5[1:-1] == szo_3:
                words.append(szo_5)
        if len(words) > 1:
            out = '\n'.join(words) + '\n' * 2
            fout.write(out)
