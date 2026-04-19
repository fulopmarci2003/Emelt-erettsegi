import math

def rendezo_mezo(lista):
    return lista[2]

f= open('sms.txt')
smsszam=int(f.readline())
print(smsszam)
smsek=[]
for i in range(smsszam):
    sor=f.readline().strip().split()
    sor2=f.readline().strip()
    sor.append(sor2)
    smsek.append(sor)
print(smsek)
f.close()

print('2. feladat')
if smsszam<10:
    print(smsek[smsszam-1][3])
else:
    print(smsek[9][3])

print('3. feladat')
maxhosszindex=0
minhosszindex=0
for i in range(smsszam):
    if len(smsek[i][3])>len(smsek[maxhosszindex][3]):
        maxhosszindex=i
    if len(smsek[i][3]) < len(smsek[minhosszindex][3]):
        minhosszindex = i
print(smsek[maxhosszindex])
print(smsek[minhosszindex])

print('4 feladat')
intervallum={'1':0,'2':0,'3':0,'4':0,'5':0,}
for i in range(smsszam):
    intervallum[str(math.ceil(len(smsek[i][3])/20))]+=1

for i in range(5):
    print(i*20+1,'-',i*20+20,intervallum[str(i+1)],'darab')

print('5. feladat')
ora=int(smsek[0][0])+1
i=0
j=0
while i<smsszam:
    if int(smsek[i][0])<ora and j<10:
        j+=1
    if j==10:
        j=0
        ora+=1
    i+=1
print(j)

print('6. feladat')
volt=False
kul=0
for i in range(smsszam):
    if smsek[i][2]=='123456789':
        if not volt:
            regiido=int(smsek[i][0])*60+int(smsek[i][1])
            volt=True
        else:
            ujido = int(smsek[i][0])*60+int(smsek[i][1])
            if kul<ujido-regiido:
                kul=ujido-regiido
if kul==0:
    print('Nincs elegendő üzenet.')
else:
    print(kul//60,':',kul%60)

print('7. feladat')
ora=input('Óra:')
perc=input('Perc:')
telefonszam=input('Telefonszám:')
szoveg=input('Az SMS szövege:')
ujsor=[ora,perc,telefonszam,szoveg]
smsek.append(ujsor)

print('8. feladat')
f=open('smski.txt','w')

smsek.sort(key=rendezo_mezo)
print(smsek[0][2])
print('\t',smsek[0][0],smsek[0][1],smsek[0][3])
f.write(smsek[0][2]+'\n')
f.write('\t'+smsek[0][0]+' '+smsek[0][1]+' '+smsek[0][3]+'\n')

for i in range(1,smsszam):
    if smsek[i][2]==smsek[i-1][2]:
        print('\t', smsek[i][0], smsek[i][1], smsek[i][3])
        f.write('\t'+smsek[i][0]+' '+smsek[i][1]+' '+smsek[i][3]+'\n')
    else:
        print(smsek[i][2])
        f.write(smsek[i][2]+'\n')
        print('\t', smsek[i][0], smsek[i][1], smsek[i][3])
        f.write('\t'+smsek[i][0]+' '+smsek[i][1]+' '+smsek[i][3]+'\n')
f.close()