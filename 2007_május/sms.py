adatok = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
          6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

print('1. feladat')
betu = input('Adjon meg egy betűt!')
for szam, adat in adatok.items():
    if betu in adat:
        print(szam)

print('2. feladat')
szo = input('Adjon meg egy szót!')
for betu in list(szo):
    for szam, adat in adatok.items():
        if betu in adat:
            print(szam, end='')

#print('\n3. feladat')
with open('szavak.txt', 'r', encoding='utf-8') as fin:
    szavak = []
    for szo in fin:
        szavak.append(szo.strip())

print('\n4. feladat')
hosz = max(szavak, key=len)
print(hosz, len(hosz))

print('5. feladat')
db = len([szo for szo in szavak if len(szo) <= 5])
print(db)

#print('6. feladat')
with open('kodok.txt', 'w', encoding='utf-8') as fout:
    for szo in szavak:
        out = ''
        for betu in list(szo):
            for szam, adat in adatok.items():
                if betu in adat:
                    out += str(szam)
        fout.write(out + '\n')

print('7. feladat')
szamsor = input('adjon meg egy számsort!')
for szo in szavak:
    out = ''
    for betu in list(szo):
        for szam, adat in adatok.items():
            if betu in adat:
                out += str(szam)
    if szamsor == out:
        print(szo)

print('8. feladat')
summa, jok = [], [[1, 1]]
for szo in szavak:
    out = ''
    for betu in list(szo):
        for szam, adat in adatok.items():
            if betu in adat:
                out += str(szam)
    summa.append([szo, out])
summa.sort(key=lambda x: int(x[1]))
for i in range(len(summa) - 1):
    if summa[i][1] == summa[i + 1][1] or summa[i][1] in list(zip(*jok))[1]:
        jok.append(summa[i])
jok.pop(0)
for szo, szam in jok:
    print(szo, szam, sep=' : ', end='; ')

print('9. feladat')
szamok = list(map(int, list(zip(*summa))[1]))
legtobb = max(set(szamok), key=szamok.count)
for szo, szam in summa:
    if int(szam) == legtobb:
        print(szo)
print(legtobb)
