def molt_szamitas(atomok):
    return atomok[0]*12+atomok[1]*1+atomok[2]*16+atomok[3]*14+atomok[4]*32

def rendezes(aminosavak):
    return aminosavak[7]

aminosavak = []
f = open('aminosav.txt')
while True:
    sor = []
    adat = f.readline()
    if adat:
        sor.append(adat.strip())
        adat = f.readline()
        sor.append(adat.strip())
        for _ in range(5):
            adat = f.readline()
            sor.append(int(adat.strip()))
        sor.append(molt_szamitas(sor[2:7]))
        aminosavak.append(sor)
    else:
        break
print(aminosavak)
f.close()

print('3. feladat')
f = open('eredmeny.txt','w')
aminosavak.sort(key=rendezes)
for sav in aminosavak:
    print(sav[0],sav[7])
    f.write(str(sav[0])+' '+str(sav[7])+'\n')

f.close()

print('4. feladat')
f = open('bsa.txt')
bsa=f.read().split()
f.close()
csz=0
hsz=0
osz=0
nsz=0
ssz=0
for aszam in bsa:
    for aminosav in aminosavak:
        if aminosav[1]==aszam:
            csz+=aminosav[2]
            hsz+=aminosav[3]
            osz+=aminosav[4]
            nsz+=aminosav[5]
            ssz+=aminosav[6]

print('C',csz,'H',hsz-2*(len(bsa)-1),'O',osz-len(bsa)+1,'N',nsz,'S',ssz)

f = open('eredmeny.txt','a')
f.write('C '+str(csz)+' H '+str(hsz-2*(len(bsa)-1))+' O '+str(osz-len(bsa)+1)+' N '+str(nsz)+ ' S '+str(ssz)+'\n')
f.close()

print('5. feladat')
kezdet=0
maxhossz=0
for i,kar in enumerate(bsa):
    if kar =='Y' or kar=='W' or kar=='F':
        vege=i
        hossz=vege-kezdet
        if hossz>maxhossz:
            maxhossz=hossz
            maxkezdet=kezdet
            maxvege=vege
        kezdet=i+1
print('A legnagyobb hossz:',maxhossz,' kezdete ', maxkezdet+1,' vége ',maxvege+1)

print('6. feladat')
for i,kar in enumerate(bsa):
    if kar=='R' and (bsa[i+1]=='A' or bsa[i+1]=='V'):
        break
if i<len(bsa):
    factor=bsa[0:i]
    print('A fehérjeláncban {0} Ciszterin található.'.format(factor.count('C')))
else:
    print('Nem történt hasítás')