with open('fogado.txt', 'r', encoding='utf-8') as f:
    foglalasok = []
    for sor in f:
        foglalasok.append(sor.strip().split())

print('2. feladat')
print(f'Foglalások száma: {len(foglalasok)}')

print('3. feladat')
nev = input('Adjon meg egy nevet:')
db = 0
for foglalas in foglalasok:
    if ' '.join(foglalas[:2]) == nev:
        db += 1
print(f'{nev} néven {db} időpontfoglalás van.' if db else 'A megadott néven nincs időpontfoglalás.')

print('4. feladat')
ido = input('Adjon meg egy érvényes időpontot (pl. 17:10):')
tanarok = []
for foglalas in foglalasok:
    if foglalas[2] == ido:
        tanarok.append(' '.join(foglalas[:2]))
with open(f'{ido.replace(":", "")}.txt', 'w', encoding='utf-8') as f:
    for tanar in sorted(tanarok):
        print(tanar)
        f.write(tanar + '\n')

print('5. feladat')
elso = sorted(foglalasok, key=lambda x: x[3])[0]
print(f'Tanár neve: {" ".join(elso[:2])}')
print(f'Foglalt időpont: {elso[2]}')
print(f'Foglalás ideje: {elso[3]}')

print('6. feladat')
eszter = list(filter(lambda x: ' '.join(x[:2]) == 'Barna Eszter', foglalasok))
eszterido = set(list(zip(*eszter))[2])
osszesido = set()
for i in range(1600, 1800, 10):
    if int(str(i)[2:]) <= 50:
        osszesido.add(str(i)[:2] + ':' + str(i)[2:])
print(*sorted(list((osszesido - eszterido))), sep='\n')
print(f'Barna Eszter legkorábban távozhat: {sorted(eszterido)[-1][:3]}{int(sorted(eszterido)[-1][3:]) + 10}')
