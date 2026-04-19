def tomeg(lst):
    return lst[2]*12 + lst[3]*1 + lst[4]*16 + lst[5]*14 + lst[6]*32

with open('aminosav.txt', 'r', encoding='utf-8') as fin:
    counter, savak, sav = 0, [], []
    for sor in fin:
        if counter < 7:
            sav.append(sor.strip())
            counter += 1
        else:
            sav[2:] = list(map(int, sav[2:]))
            savak.append(sav)
            sav = []
            sav.append(sor.strip())
            counter = 1

with open('eredmeny.txt', 'w', encoding='utf-8') as fout:
    print('2. feladat')
    fout.write('2. feladat\n')
    for sav in savak:
        print(tomeg(sav))
        fout.write(str(tomeg(sav)) + '\n')

    print('3. feladat')
    fout.write('3. feladat\n')
    for sav in sorted(savak, key=lambda x: tomeg(x)):
        print(sav[0], tomeg(sav), sep=' ')
        fout.write(sav[0] + ' ' + str(tomeg(sav)) + '\n')

with open('bsa.txt', 'r', encoding='utf-8') as fin:
    bsa, elemek = [], [0, 0, 0, 0, 0]
    for sor in fin:
        bsa.append(sor.strip())

    for elem in bsa:
        for sav in savak:
            if elem == sav[1]:
                elemek[0] += sav[2]
                elemek[1] += sav[3]
                elemek[2] += sav[4]
                elemek[3] += sav[5]
                elemek[4] += sav[6]
    elemek[1] -= 2 * (len(bsa) - 1)
    elemek[2] -= (len(bsa) - 1)

with open('eredmeny.txt', 'a', encoding='utf-8') as fout:
    print('4. feladat')
    fout.write('4. feladat\n')
    print(f'C {elemek[0]} H {elemek[1]} O {elemek[2]} N {elemek[3]} S {elemek[4]}')
    fout.write(f'C {elemek[0]} H {elemek[1]} O {elemek[2]} N {elemek[3]} S {elemek[4]}\n')

savak_1, sav_1 = [], []
for sav in bsa:
    if sav not in ['Y', 'W', 'F']:
        sav_1.append(sav)
    else:
        sav_1.append(sav)
        savak_1.append(sav_1)
        sav_1 = []
if bsa[-1] not in ['Y', 'W', 'F']:
    savak_1.append(sav_1)

lanc = sorted(savak_1, key=len, reverse=True)[0]
hely = savak_1.index(lanc)
kezdes = sum([len(sav) for sav in savak_1[:hely]]) + 1
veg = kezdes + len(lanc)
print('5. feladat')
print(f'A lánc hossza: {len(lanc)}')
print(f'A lánc kezdete: {kezdes}')
print(f'A lánc vége: {veg}')