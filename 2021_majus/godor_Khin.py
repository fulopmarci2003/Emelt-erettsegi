print('1. feladat')
melyseg=[]
with open('melyseg.txt','r') as f:
    for sor in f:
        melyseg.append(int(sor.strip()))
# print(melyseg)
print('Adatok száma: ',len(melyseg))
print('2. feladat')
tavolsag = int(input('Távolság: '))-1   ###Mert melyseg[0] az első méter
print('Ezen a helyen a felszín {} m mélyen van.'.format(melyseg[tavolsag-1]))
print('3. feladat')
###Ahol a melyseg listába 0 van , ott érintetlen. Ezeket a helyeket kell megszámlálni
erintetlen = 0
for sor in melyseg:
    if sor == 0:
        erintetlen +=1
print('Az érintetlen terület arány {}%.'.format(round(erintetlen/len(melyseg)*100, 2)))

######VAGY

print('Az érintetlen terület arány {}%.'.format(round(melyseg.count(0)/len(melyseg)*100, 2)))
print('4. feladat')
f = open('godrok.txt', 'w', encoding='utf-8')
i = 0    # A lista hányadik eleménél tartunk
godrokszama = 0  # Hány gödör van
sor = []  # Ebben gyüjtjük egy-egy gödör adatait
while melyseg[i] == 0:  # Keressük az első gödör szélét
    i += 1
while i < len(melyseg)-1:   # amíg nem vagyunk a lista végén...
    sor = []    #új gödör kezdődik
    while melyseg[i] != 0:    # amíg meg nem találtuk a másik szélét...
        sor.append(melyseg[i])
        i += 1
    # print(' '.join(list(map(str,sor))))
    f.write(' '.join(list(map(str,sor)))+'\n')   ##itt a másik széle, kiírjuk a file-ba
    godrokszama += 1    # Volt egy gödör!!!
    while melyseg[i] == 0 and i < len(melyseg)-1:  #ellépkedünk a következő gödör széléig vagy a lista végéig
        i += 1
f.close()
print('5. feladat')
print('A gödrök száma:',godrokszama)
print('6. feladat')
eleje=vege=tavolsag
if melyseg[tavolsag] == 0:
    print('Az adott helyen nincs gödör.')
else:
    legmelyebb = melyseg[tavolsag]  # Indulásnál ez a legmélyebb pont
    legmelyebbhelye=tavolsag
    while melyseg[eleje] != 0:    # Keressük a gödör elejét
        if melyseg[eleje] > legmelyebb:    # Vizsgáljuk, hogy mélyebb-e, mint az eddigi legmélyebb
            legmelyebb = melyseg[eleje]
            legmelyebbhelye = eleje
        eleje -= 1  # megyünk a gödör eleje felé
    while melyseg[vege] != 0:       #Keressük a gödör végét
        if melyseg[vege] > legmelyebb:  # Vizsgáljuk, hogy mélyebb-e, mint az eddigi legmélyebb
            legmelyebb = melyseg[vege]
            legmelyebbhelye = vege
        vege += 1   #megyünk a gödör vége felé
    print('a)\nA gödör kezdete: {} méter, a gödör vége: {} méter'.format(eleje+2,vege))
    #Azért eleje+2, mert a gödör bal szélétől 1-el balra áll meg (+1) és a lista indexelése 0-val kezdődik (+1)
    #Azért vege, mert a gödör jobb szélétől 1-el jobbra áll meg (-1) és a lista indexelése 0-val kezdődik (+1)
    monoton = True
    terfogat = 0
    for i in range(eleje+1,legmelyebbhelye):   #haladunk az elejétől a legmélyebb pontig
        terfogat += melyseg[i]  # kiszámoljuk a térfogatát
        if melyseg[i]>melyseg[i+1]:
            monoton = False
    for i in range(legmelyebbhelye,vege): #haladunk a legmélyebbtől a végéig
        terfogat += melyseg[i]
        if melyseg[i] < melyseg[i + 1]:
            monoton = False
    terfogat += melyseg[vege]   # a gödör szélén levő mélységet még hozzá kell adni
    print('b)\nFolyamatosan mélyül' if (monoton) else 'b)\nNem mélyül folyamatosan.')
    print('c)\nA legnagyobb mélysége {} méter.'.format(legmelyebb))
    print('d)\nA térfogata {} m^3.'.format(terfogat*10))
    vizmennyiseg = 0
    for i in range(eleje+1,vege+1):   #végighaladunk a gödrön
        if melyseg[i] != 0:
            vizmennyiseg += melyseg[i]-1   # 1 méterrel kevesebb vizzel kell számolni
    print('e)\nA vízmennyisége {} m^3.'.format(vizmennyiseg * 10))

    ###VAGY

    print('e)\nA vízmennyisége {} m^3.'.format((terfogat - (vege - (eleje + 1))) * 10))
