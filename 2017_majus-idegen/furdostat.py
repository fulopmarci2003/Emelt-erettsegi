
with open("furdoadat.txt", "r", encoding='utf-8') as fin:
    adatok = []
    for sor in fin:
        adatok.append(list(map(int, sor.strip().split())))

print('2. feladat')
print(f'Az első vendég {adatok[0][3]}:{adatok[0][4]}:{adatok[0][5]}-kor lépett ki az öltözőből.')
for adat in reversed(adatok):
    if adat[1] == 0 and adat[2] == 1:
        ora, perc, mperc = adat[3:]
        break
print(f'Az utolsó vendég {ora}:{perc}:{mperc}-kor lépett ki az öltözőből.')

print('3. feladat')
idk = list(zip(*adatok))[0]
db = 0
for setid in set(idk):
    if idk.count(setid) == 4:
        db += 1
print(f'A fürdőben {db} vendég járt csak egy részlegen.')

print('4. feladat')
maxido = 0
for setid in set(idk):
    egyid = list(filter(lambda x: x[0] == setid, adatok))
    if (egyid[-1][3] * 3600 + egyid[-1][4] * 60 + egyid[-1][5]) - (egyid[0][3] * 3600 + egyid[0][4] * 60 + egyid[0][5]) > maxido:
        maxido = (egyid[-1][3] * 3600 + egyid[-1][4] * 60 + egyid[-1][5]) - (egyid[0][3] * 3600 + egyid[0][4] * 60 + egyid[0][5])
        id = setid
ora = maxido//3600
perc = (maxido - ora*3600)//60
mperc = maxido - ora*3600 - perc*60
print(f'A legtöbb időt eltöltő vendég:\n{id}. vendég {ora}:{perc}:{mperc}')

print('5. feladat')
erk1, erk2, erk3 =0, 0, 0
for adat in adatok:
    if adat[1] == 0 and adat[2] == 1 and (6*3600 <= adat[3]*3600 + adat[4]*60 + adat[5] < 9*3600):
        erk1 += 1
    elif adat[1] == 0 and adat[2] == 1 and (9*3600 <= adat[3]*3600 + adat[4]*60 + adat[5] < 16*3600):
        erk2 += 1
    elif adat[1] == 0 and adat[2] == 1 and (16*3600 <= adat[3]*3600 + adat[4]*60 + adat[5] < 20*3600):
        erk3 += 1
print(f'6-9 óra között {erk1} vendég')
print(f'9-16 óra között {erk2} vendég')
print(f'16-20 óra között {erk3} vendég')

with open('szauna.txt', 'w', encoding='utf-8') as fout:
    for setid in set(idk):
        szauna = list(filter(lambda x: x[0] == setid and x[1] == 2, adatok))
        osszido = 0
        for i in range(0, len(szauna), 2):
            osszido += (szauna[i + 1][3]*3600 + szauna[i + 1][4]*60 + szauna[i + 1][5]) - (szauna[i][3]*3600 + szauna[i][4]*60 + szauna[i][5])
        ora = osszido // 3600
        perc = (osszido - ora * 3600) // 60
        mperc = osszido - ora * 3600 - perc * 60
        fout.write(f'{setid} {ora}:{perc}:{mperc}\n')

print('7. feladat')
usz, szau, gyogy, strand = 0, 0, 0, 0
for setid in set(idk):
    type_by_id = [adat[1] for adat in adatok if adat[0] == setid]
    if 1 in type_by_id:
        usz += 1
    if 2 in type_by_id:
        szau += 1
    if 3 in type_by_id:
        gyogy += 1
    if 4 in type_by_id:
        strand += 1
print(f'Uszoda: {usz}\nSzaunák: {szau}\nGyógyvizes medencék: {gyogy}\nStrand: {strand}')

