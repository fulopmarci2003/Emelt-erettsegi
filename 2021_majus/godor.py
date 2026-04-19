with open("melyseg.txt", "r", encoding="utf-8") as in_file:
    values = [int(i) for i in in_file.read().split()] # values = list(map(int, in_file.read().split()))
print(f'1. feladat\nA fájl adatainak száma: {len(values)}')
in_data = int(input('\n2. feladat\nAdjon meg egy távolságértéket!'))
print(f'Ezen a helyen a felszín {values[in_data]} méter mélyen van.\n\n3. feladat\nAz érintetlen terület aránya {round(values.count(0)/len(values)*100, 2)} %\n')
dict_values, is_null, output = {}, True, ''
for i, data in enumerate(values):
    if data != 0 and is_null:
        index_start, is_null = i, False
    if data == 0 and not is_null:
        index_end, is_null = i, True
        dict_values[index_start] = index_end
print(f'5. feladat\nA gödrök száma: {len(dict_values)}\n')
with open("godrok.txt", "w", encoding="utf-8") as out_file:
    for key, value in dict_values.items():
        output += (str(values[key:value]).replace('[', '').replace(']', '') + '\n')
    out_file.write(output[0:-1])
if values[in_data] != 0:
    for key_2, value_2 in dict_values.items():
        if key_2 <= in_data <= value_2:
            print(f'6. feladat\na)\nA gödör kezdete {key_2 + 1} méter, a gödör vége {value_2} méter\nb)')
            godor_start, godor_end = key_2, value_2
    list_godor = values[godor_start:godor_end]
    maxindex, is_more, is_less = 0, False, False
    for h, data in enumerate(list_godor):
        maxindex = h if data > list_godor[maxindex] else maxindex
    for l in range(0, maxindex):
        is_more = True if list_godor[l] > list_godor[l+1] else is_more
    for n in range(maxindex, len(list_godor) - 1):
        is_less = True if list_godor[n] < list_godor[n+1] else is_less
    print('Folyamatosan mélyül.') if not is_more and not is_less else print('Nem mélyül folyamatosan.')
    print(f'c)\nA legnagyobb mélysége {max(list_godor)} méter.\nd)\nA térfogata {sum(list_godor)*10} m^3.\ne)\nA vízmennyiség {(sum(list_godor) - (godor_end - godor_start)) * 10} m^3.')
else:
    print("Az adott helyen nincs gödör")