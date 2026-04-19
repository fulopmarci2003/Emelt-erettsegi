import math
f = open('eladott.txt')
sor = f.readline().strip().split()
jegyek_szama= int(sor[0])
uthossz=int(sor[1])
egysegar=int(sor[2])
utasok=[]
for _ in range(jegyek_szama):
    sor = list(map(int,f.readline().strip().split()))
    utasok.append(sor)
f.close()

print('2. feladat')
print('Az utolsó jegyvásárló székszáma: ',utasok[jegyek_szama-1][0])
print('Az általa megtett út:',utasok[jegyek_szama-1][2]-utasok[jegyek_szama-1][1])

print('3. feladat')
for index,utas in enumerate(utasok):
    if utas[1]==0 and utas[2]==uthossz:
        print(index+1, end=' ')

print('4. feladat')

def fizetendo(l,f):
    ut=l[2]-l[1]
    ut10=math.ceil(ut/10)
    fiz=ut10*f
    m=fiz%5
    if m>0 and m<3:
        fiz=fiz-m
    elif m>2 and m<5:
        fiz=fiz-m+5
    return fiz

bevetel=0
for  utas in utasok:
    bevetel+=fizetendo(utas,egysegar)
print('A társaság bevétele:',bevetel)

print('5. feladat')
#halmazba teszzuk, hogy ne legyen ismetlodes
felszallok={utas[1]  for utas in utasok}
leszallok={utas[2]  for utas in utasok}
megallok=sorted(list(felszallok|leszallok))
felsz_utolso=0
lesz_utolso=0
for utas in utasok:
    if utas[1]==megallok[-2]:
        felsz_utolso+=1
    if utas[2]==megallok[-2]:
        lesz_utolso+=1
print('Leszállók száma: {0} Felszállók száma: {1}'.format(lesz_utolso,felsz_utolso))

print('6. feladat')
print('A kiinduló és a célállomás közötti megállok száma:',len(megallok)-2)

print('7. feladat')
f= open('kihol_2.txt','w',encoding='UTF8')
tav=int(input('Kérem a távolságot:'))
ulesek=[]
for i,utas in enumerate(utasok):
    if utas[1]<=tav and utas[2]>tav:
        ulesek.append([utas[0],i+1])
ulesek=sorted(ulesek)
j=1
for ules in ulesek:
    if ules[0]==j:
        f.write(str(j)+'. ülés: '+str(ules[1])+'. utas\n')
#       print(j,ules[1])
        j+=1
    else:
        while j<ules[0]:
            f.write(str(j)+'. ülés: üres\n')
#            print(j,'Üres')
            j+=1
        f.write(str(j) + '. ülés: ' + str(ules[1]) + '. utas\n')
        #        print(j, ules[1])
        j += 1
while j<49:
    f.write(str(j) + '. ülés: üres\n')
    j+=1
f.close()