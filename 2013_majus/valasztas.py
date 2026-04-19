#1.feladat
with open('szavazatok.txt', 'r', encoding='utf-8') as fin:
    szavazatok = []
    for sor in fin:
        readline = sor.strip().split()
        szavazatok.append([int(readline[0]), int(readline[1]), f'{readline[2]} {readline[3]}', 'fuggetlen' if readline[4] == '-' else readline[4]])

#2.feladat
print(f'A helyhatósági választáson {len(szavazatok)} képviselőjelölt indult.')

#3.feladat
vez_nev = input('Adj meg egy vezeteknevet!')
ut_nev = input('Adj meg egy keresztnevet!')
for szavazat in szavazatok:
    if f'{vez_nev} {ut_nev}' == szavazat[2]:
        print(f'{vez_nev} {ut_nev} {szavazat[1]} szavazatot kapott!')
        break
else:
    print('Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!')

#4.feladat
votes = 0
for szavazat in szavazatok:
    votes += szavazat[1]
print(f'A választáson {votes} állampolgár, a jogosultak {(votes/12345) * 100:.2f}%-a vett részt.')

#5.feladat
pártnevek = {'ZEP': 'Zöldségevők Pártja', 'TISZ': 'Tejivók Szövetsége', 'GYEP': 'Gyümölcsevők Pártja', 'HEP': 'Húsevők Pártja', 'fuggetlen': 'Független jelöltek'}
ZEP, TISZ, GYEP, HEP, fuggetlen = 0, 0, 0, 0, 0
for párt in pártnevek.keys():
    for szavazat in szavazatok:
        if szavazat[3] == párt:
            locals()[párt] += szavazat[1]
    print(f'{pártnevek[párt]} = {(locals()[párt]/votes) * 100:.2f}%')

#6.feladat
for szavazat in szavazatok:
    if szavazat[1] == max(list(zip(*szavazatok))[1]):
        print(szavazat[2], szavazat[3], sep='\t')

#7.feladat
with open('kepviselok.txt', 'w', encoding='utf-8') as fout:
    for korzet in range(1, 9):
        max_szavazat_index = 0
        for i, szavazat in enumerate(szavazatok):
            if szavazat[0] == korzet and szavazat[1] > szavazatok[max_szavazat_index][1]:
                max_szavazat_index = i
        fout.write(f'{szavazatok[max_szavazat_index][2]} {szavazatok[max_szavazat_index][3]}\n')