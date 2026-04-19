import string
import random
with open('kerites.txt') as f:
    keritesek = []
    for sor in f:
        sor = sor.strip().split()
        sor[:2] = list(map(int, sor[:2]))
        keritesek.append(sor)

print('2. feladat')
print(f'Az eladott telkek száma: {len(keritesek)}')

print('3. feladat')
print(f'A {"páratlan" if keritesek[-1][0] else "páros"} oldalon adták el az utolsó telket.')
print(f'Az utolsó telek házszáma: {list(zip(*keritesek))[0].count(keritesek[-1][0]) * 2 - int(keritesek[-1][0])}')

print('4. feladat')
paratlan = list(filter(lambda x: x[0] == 1, keritesek))
for i in range(len(paratlan) - 1):
    if paratlan[i][2] == paratlan[i + 1][2] and paratlan[i][2] not in ['#', ':']:
        print(f'A szomszédossal egyezik a kerítés színe: {i * 2 + 1}')
        break

print('5. feladat')
hazszam = int(input('Adjon meg egy házszámot!'))
szin = []
if hazszam % 2 == 0:
    szinek = list(zip(*list(filter(lambda x: x[0] == 0, keritesek))))[2]
    print(f'A kerítés színe / állapota:{szinek[int(hazszam / 2) - 1]}')
    if hazszam != 2:
        szin.extend(szinek[int(hazszam / 2) - 2:int(hazszam / 2) + 1])
    else:
        szin.extend(szinek[int(hazszam / 2) - 1:int(hazszam / 2) + 1])

else:
    szinek = list(zip(*list(filter(lambda x: x[0] == 1, keritesek))))[2]
    print(f'A kerítés színe / állapota:{szinek[int((hazszam - 1) / 2)]}')
    if hazszam != 1:
        szin.extend(szinek[int((hazszam - 1) / 2) - 1:int((hazszam - 1) / 2) + 2])
    else:
        szin.extend(szinek[int((hazszam - 1) / 2):int((hazszam - 1) / 2) + 2])
print(f'Egy lehetséges festési szín: {random.choice(list(set(string.ascii_uppercase) - set(szin)))}')

with open('utcakep.txt', 'w', encoding='utf-8') as f:
    szin = db = ''
    for i, kerites in enumerate(list(filter(lambda x: x[0] == 1, keritesek)), start=1):
        szin += kerites[2] * int(kerites[1])
        db += str(i * 2 - 1) + ' ' * (kerites[1] - len(str(i * 2 - 1)))
    f.write(szin + '\n' + db)
