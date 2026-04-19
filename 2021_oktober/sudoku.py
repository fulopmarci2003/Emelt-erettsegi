print('1. feladat')
file = input('Adja meg a bemeneti fájl nevét!')
sor = int(input('Adja meg egy sor számát!'))
oszlop = int(input('Adja meg egy oszlop számát!'))

with open(file, 'r', encoding='utf-8') as fin:
    adat = []
    for szam in fin:
        adat.append(list(map(int, szam.strip().split())))
    sudoku = adat[:9]
    szamok = adat[9:]

print('3. feladat')
if sudoku[sor - 1][oszlop - 1]:
    print(f'Az adott helyen szereplő szám: {sudoku[sor - 1][oszlop - 1]}')
else:
    print('Az adott helyet még nem töltötték ki.')
minta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'A hely a(z) {minta[(sor - 1)//3][(oszlop - 1)//3]} résztáblázathoz tartozik.')

print('4. feladat')
nulla = 0
for szam in sudoku:
    nulla += szam.count(0)
print(f'Az üres helyek aránya: {(nulla/81) * 100:.1f}%')

print('5. feladat')
for szam in szamok:
     resztabla = []
     resz = []
     for i in sudoku[((szam[1] - 1)//3) * 3:((szam[1] - 1)//3) * 3 + 3]:
         resztabla.append(i[((szam[2] - 1)//3) * 3:((szam[2] - 1)//3) * 3 + 3])
     for a in resztabla:
        for b in a:
            resz.append(b)
     print(f'A kiválasztott sor: {szam[1]} oszlop: {szam[2]} a szám: {szam[0]}')
     if sudoku[szam[1] - 1][szam[2] - 1] != 0:
         print('A helyet már kitöltötték\n')
     elif szam[0] in sudoku[szam[1] - 1]:
         print('Az adott sorban már szerepel a szám\n')
     elif szam[0] in list(zip(*sudoku))[szam[2] - 1]:
         print('Az adott oszlopban már szerepel a szám\n')
     elif szam[0] in resz:
         print('Az adott résztáblázatban már szerepel a szám\n')
     else:
         print('A lépés megtehető\n')