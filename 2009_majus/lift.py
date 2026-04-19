import random
#1. feladat
with open('igeny.txt', 'r', encoding='utf-8') as fin:
    max_szint = int(fin.readline().strip())
    max_csapat = int(fin.readline().strip())
    max_igeny = int(fin.readline().strip())
    igenyek = []
    for sor in fin:
        igenyek.append(list(map(int, sor.strip().split())))

#2. feladat
print('2. feladat')
kezdo_szint = int(input(f'Kérem a lift indulási helyét! (0 - {max_szint})'))

#3. feladat
print('3. feladat')
print(f'A lift a {igenyek[-1][-1]}. szinten áll az utolsó igény teljesítése után.')

#4. feladat
print('4. feladat')
start, stop = list(zip(*igenyek))[4:6]
print(f'A legalacsonyabb sorszámú szint: {min(start + stop)}')
print(f'A legmagasabb sorszámú szint: {max(start + stop)}')

#5. feladat
print('5. feladat')
fel_utasnelkul, fel_utassal = 0, 0
for i in range(len(igenyek) - 1):
    if igenyek[i][5] < igenyek[i + 1][4]:
        fel_utasnelkul += 1
if kezdo_szint < igenyek[0][4]:
    fel_utasnelkul += 1
for igeny in igenyek:
    if igeny[4] < igeny[5]:
        fel_utassal += 1
print(f'Felfelé indulások száma utassal: {fel_utassal}')
print(f'Felfelé indulások száma utas nélkül: {fel_utasnelkul}')

#6. feladat
print('6. feladat')
print(*set(range(1, max_csapat + 1)) - set(list(zip(*igenyek))[3]))

#7. feladat
print('7. feladat')
szabalyos = True
veletlen_csapat = random.choice(list(zip(*igenyek))[3])
igenyek_by_veletlencsapat = [igeny for igeny in igenyek if igeny[3] == veletlen_csapat]
for i in range(len(igenyek_by_veletlencsapat) - 1):
    if igenyek_by_veletlencsapat[i][5] != igenyek_by_veletlencsapat[i + 1][4]:
        szabalyos = False
        a, b = igenyek_by_veletlencsapat[i][5], igenyek_by_veletlencsapat[i + 1][4]
print(f'{veletlen_csapat} számú csapat', 'Nem bizonyítható szabálytalanság' if szabalyos else f'{a} --> {b}', sep=': ')

#8. feladat
out = ''
for i in range(len(igenyek_by_veletlencsapat)):
    igenyek_by_veletlencsapat[i].append(input('Adja meg, sikeres e a munka'))
with open('blokkol.txt', 'w', encoding='utf-8') as fout:
    for igeny in igenyek_by_veletlencsapat:
        out += f'Indulási emelet: {igeny[4]}\n\
Célemelet: {igeny[5]}\n\
Feladatkód: {random.randint(1, 99)}\n\
Befejezés ideje: {igeny[0]}:{igeny[1]}:{igeny[2]}\n\
Sikeresség: {igeny[6]}\n\
-----\n'
    fout.write(out[:-7])