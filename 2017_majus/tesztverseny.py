def calculator(megoldas, helyes):
    summa = 0
    valasz_helyes = str(helyes).replace('', ' ').split()
    valasz = str(megoldas).replace('', ' ').split()
    for k in range(len(valasz)):
        if valasz[k] == valasz_helyes[k] and k <= 4:
            summa += 3
        elif valasz[k] == valasz_helyes[k] and 5 <= k <= 9:
            summa += 4
        elif valasz[k] == valasz_helyes[k] and 10 <= k <= 12:
            summa += 5
        elif valasz[k] == valasz_helyes[k] and k == 13:
            summa += 6
    return summa
with open("valaszok.txt", "r", encoding="utf-8") as in_file:
    key = in_file.readline().strip()
    list_key = key.replace('', ' ').split()
    in_data = in_file.readline().split()
    list_main = []
    while in_data:
        list_main.append(in_data)
        in_data = in_file.readline().split()
print(f'1. feladat: Az adatok beolvasása\n\n2. feladat: A vetélkedőn {len(list_main)} versenyző indult.')
person = input('\n3. feladat: A versenyző azonosítója = ')
for data in list_main:
    if data[0] == person:
        print(f'{data[1]}\t(a versenyző válasza)')
        ans = data[1].replace('', ' ').split()
        break #nem kötelező, de gyorsítja a programot!
output_file = ''
for i in range(len(list_key)):
    output_file += '+' if ans[i] == list_key[i] else ' '
print(f'\n4. feladat:\n{key}  (a helyes megoldás)\n{output_file}  (a versenyző helyes válaszai)')
sorszam = int(input('\n5. feladat: A feladat sorszáma = '))
megoldas = 0
for data in list_main:
     megoldas += 1 if data[1][sorszam - 1] == list_key[sorszam - 1] else 0
print(f'A feladatra {megoldas} fő, a versenyzők {round(megoldas/len(list_main)*100, 2)}%-a adott helyes választ.\n\n6. feladat: A versenyzők pontszámának meghatározása\n\n7. feladat: A verseny legjobbjai:')
with open('pontok.txt', 'w', encoding='utf-8') as out_file:
    for data in list_main:
        out_file.writelines(f'{data[0]} {calculator(data[1], key)}\n')
for data in list_main:
   data[1] = calculator(data[1], key)
list_main.sort(key=lambda x: x[1], reverse=True)
for i, data in enumerate(list_main, start=1):
    print(f'{i}. díj ({data[1]} pont): {data[0]}')
    if i == 4:
        break
