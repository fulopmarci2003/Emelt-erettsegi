import os

def mpbe(o,p,mp):
    return o*3600+p*60+mp
def mpbol(ertek):
    o = ertek // 3600
    ertek = ertek % 3600
    p = ertek // 60
    mp = ertek % 60
    return [o,p,mp]

#os.system('pause')


print('1. feladat')
adatok=[]
f = open('furdoadat.txt')
for sor in f:
    adatok.append(list(map(int,sor.strip().split())))

# sor[0] --> vendégazonosító
# sor[1] --> részlegazonosító
# sor[2] --> be, vagy kilépés -- 0, ha belépett
# sor[3] -->óra
# sor[4] -->perc
# sor[5] -->másodperc

print('2. feladat')
print('Az első vendég',':'.join(list(map(str,adatok[0][3:6]))),'-kor lépett ki az öltözőből')
# Mivel az adatállomány utolsó sora az öltözőbe való
# belépés és a fürdő elhagyása, ezért előtte keressük
# az első olyan sort, ami az öltözőre vonatkozik (0)
# Az utolsó sor a -1 indexű
i=-2
sor = adatok[i]
while sor[1] != 0:
    i -= 1
    sor = adatok[i]
print('Az utolsó vendég',':'.join(list(map(str,adatok[i][3:6]))),'-kor lépett ki az öltözőből')

print('3. feladat')
#kigyűjtjük az összes azonosítót
osszes_azonosito = []
for sor in adatok:
    osszes_azonosito.append(sor[0])
# majd halmazzá alakítjuk, hogy csak az egyediek maradnak meg
vendegek = set(osszes_azonosito)

# VAGY
# vendegek = [sor[0] for sor in adatok]
# vendegek = list(set(vendegek))
# print(vendegek)


csak_egy_reszlegben = 0
# Azok jártak csak egy részlegben, akik négyszer szerepelnek
for vendeg in vendegek:
    if osszes_azonosito.count(vendeg) == 4:
        csak_egy_reszlegben += 1
print('A fürdőben {} vendég járt csak egy részlegben.'.format(csak_egy_reszlegben))

print('4. feladat')
legtobbido = 0
legtobbidoteltolto=0
for vendeg in vendegek:
    for sor in adatok:
        if sor[0] == vendeg and sor[1] == 0 and sor[2] == 1:
            erkezett = mpbe(sor[3],sor[4],sor[5])
        if sor[0] == vendeg and sor[1] == 0 and sor[2] == 0:
            tavozott = mpbe(sor[3], sor[4], sor[5])
    if tavozott - erkezett > legtobbido:
        legtobbido = tavozott - erkezett
        legtobbidoteltolto = vendeg
print('A legtöbb időt eltöltő vendég:',legtobbidoteltolto,':'.join(list(map(str,mpbol(legtobbido)))))

print('5. feladat')
erk69=erk916=erk1620=0
for sor in adatok:
    if sor [1] == 0 and sor[2] == 1:
        if sor[3] < 9:
            erk69 += 1
        elif sor[3] < 16:
            erk916 += 1
        else:
            erk1620 += 1
print('6-9 óra között érkezett ',erk69,' vendég')
print('9-16 óra között érkezett ',erk916,' vendég')
print('16-20 óra között érkezett ',erk1620,' vendég')

print('6. feladat')
f = open('szauna1.txt','w',encoding='utf-8')
for vendeg in vendegek:
    szaunaido = 0
    for sor in adatok:
        if sor[0] == vendeg and sor[1] == 2 and sor[2] == 0:
            erkezett = mpbe(sor[3], sor[4], sor[5])
        if sor[0] == vendeg and sor[1] == 2 and sor[2] == 1:
            tavozott = mpbe(sor[3], sor[4], sor[5])
            szaunaido += (tavozott-erkezett)
    if szaunaido > 0:
        f.write(str(vendeg)+' '+':'.join(list(map(str,mpbol(szaunaido))))+'\n')
f.close()

print('7. feladat')
uszoda=set()
szauna = set()
gyogyviz = set()
strand = set()
for sor in adatok:
    if sor[1] == 1:
        uszoda.add(sor[0])
    elif sor[1] == 2:
        szauna.add(sor[0])
    elif sor[1] == 3:
        gyogyviz.add(sor[0])
    elif sor[1] == 4:
        strand.add(sor[0])

print('Uszoda:',len(uszoda))
print('Szauna:',len(szauna))
print('Gyógyvizes medencék:',len(gyogyviz))
print('Strand:',len(strand))