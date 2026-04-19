def dijszamitas(tavolsag:int):
     match tavolsag:
         case 1 | 2:
             return 500
         case 3 | 4 | 5:
             return 700
         case num if num in range(6, 11):
             return 900
         case num if num in range(11, 21):
             return 1400
         case num if num in range(20, 31):
             return 2000

#1. feladat
with open('tavok.txt', 'r') as fin:
    szallitasok = []
    for sor in fin:
        szallitasok.append(list(map(int, sor.strip().split())))

szallitasok.sort()

#2. feladat
print(f'A hét legelső útja {szallitasok[0][2]} km volt.')

#3. feladat
print(f'A hét utolsó útja {szallitasok[-1][2]} km volt.')

#4. feladat
for nap in range(1, 8):
    if nap not in list(zip(*szallitasok))[0]:
        print(f'A(z) {nap}. napon volt szabadnapos a futár')

#5. feladat
print(f'A(z) {max(set(list(zip(*szallitasok))[0]), key=list(zip(*szallitasok))[0].count)}. napon volt a legtöbb fuvar')

#6. feladat
for nap in range(1, 8):
    osszes_km = 0
    for szallitas in szallitasok:
        if szallitas[0] == nap:
            osszes_km += szallitas[2]
    print(f'{nap}. nap: {osszes_km} km')

#7.feladat
tavolsag = int(input('Adjon meg egy távolságot 1-30 km között!'))
print(dijszamitas(tavolsag))

#8. feladat
with open('dijazas.txt', 'w', encoding='utf-8') as fout:
    for i in szallitasok:
        fout.write(f'{i[0]}. nap {i[1]}. út: {dijszamitas(i[2])} Ft\n')

#9. feladat
print(f'{sum([dijszamitas(szam) for szam in list(zip(*szallitasok))[2]])} Ft a futár heti bevétele.')