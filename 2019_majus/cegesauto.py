with open("autok.txt", "r", encoding="utf-8") as in_file:
    in_data = in_file.readline().split()
    list_big = []
    while in_data:
        list_big.append(in_data)
        in_data = in_file.readline().split()

    for i, data in enumerate(list_big):
        if data[5] == "0":
            ind = i

    print(f"2. feladat\n{list_big[ind][0]}.nap rendszám: {list_big[ind][2]}")

    day = input("3. feladat\nNap:")
    print(f'Forgalom {"az" if day == "1" or day == "5" else "a"} {day}. napon:')
    for data in list_big:
        if data[0] == day:
           print(f'{data[1]} {data[2]} {data[3]} {"be" if data[5] == "1" else "ki"}')
    value = 0
    for data in list_big:
        if data[5] == "1":
            value -= 1
        else:
            value += 1

    print(f'4. feladat\nA hónap végén {value} autót nem hoztak vissza\n5. feladat')
    min_km = []
    max_km = []
    for i in range(10):
       for data in list_big:
           if int(data[2][5]) == i and data[5] == "0":
               min_km.append(int(data[4]))
               break
    for i in range(10):
        for j, data in enumerate(list_big):
            if int(data[2][5]) == i and data[5] == "1":
                maxkm_index = j

        max_km.append(int(list_big[maxkm_index][4]))

    for i in range(10):
        print(f'CEG30{i} {max_km[i] - min_km[i]} km')

    list_people = []
    for data in list_big:
        if int(data[3]) not in list_people:
            list_people.append(int(data[3]))
    list_km_start = []
    list_km_end = []
    number = 0
    for people in list_people:
        for data in list_big:
            if int(data[3]) == people and data[5] == "0":
                list_km_start.append(int(data[4]))

            if int(data[3]) == people and data[5] == "1":
                list_km_end.append(int(data[4]))

        if len(list_km_start) > len(list_km_end):
            list_km_start.pop()

        for i in range(len(list_km_start)):
            distance = list_km_end[i] - list_km_start[i]
            if distance > number:
                number = distance
                driver = people

    output_file = ''
    print(f'6. feladat\nLeghosszabb út {number} km, személy: {driver}')
    rendszam = input('7. feladat\nRendszám:')
    for data in list_big:
        if data[2] == rendszam and data[5] == "0":
            output_file += (f'{data[3]} \t{data[0]}. {data[1]}\t{data[4]} km \t')
        if data[2] == rendszam and data[5] == "1":
            output_file += (f'{data[0]}. {data[1]}\t{data[4]} km\n')

with open(f'{rendszam}.txt', "w",) as out_file:
    out_file.write(output_file)
    print('Menetlevél kész.')