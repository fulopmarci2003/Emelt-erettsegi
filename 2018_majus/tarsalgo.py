def passed_time(start_time_hour, start_time_minute, end_time_hour, end_time_minute):
    return (int(end_time_hour) - int(start_time_hour)) * 60 - int(start_time_minute) + int(end_time_minute)
with open("ajto.txt", "r", encoding="utf-8") as in_file:
    in_data = in_file.readline().split()
    list_main = []
    while in_data:
        list_main.append(in_data)
        in_data = in_file.readline().split()
    for i, data in enumerate(list_main):
        if data[3] == 'ki':
            kilep = i
    print(f'2. feladat\nAz első belépő: {list_main[0][2]}\nAz utolsó belépő: {list_main[kilep][2]}')
    list_people = []
    for data in list_main:
        if int(data[2]) not in list_people:
            list_people.append(int(data[2]))
    list_people.sort()
    summa = 0
    output_file = ''
    for i in list_people:
        for data in list_main:
            if int(data[2]) == i:
                summa += 1
        output_file += (f'{i} {summa}\n')
        summa = 0
    with open("athaladas.txt", "w") as out_file:
        out_file.write(output_file)
    is_in = 0
    print('4. feladat\nA végén a társalgóban voltak: ', end="")
    for i in list_people:
        for data in list_main:
            if int(data[2]) == i and data[3] == "be":
                is_in += 1
            if int(data[2]) == i and data[3] == "ki":
                is_in -= 1
        print(i, end=" ") if is_in == 1 else ""
        is_in = 0
    people = 0
    maximum = 0
    for i, data in enumerate(list_main):
        if data[3] == "be":
            people += 1
        else:
            people -= 1
        if people > maximum:
            maximum = people
            ind = i
    print(f'\n5. feladat\nPéldául {list_main[ind][0]}:{list_main[ind][1]}-kor voltak a legtöbben a társalgóban.')
    person = input('6. feladat\nAdja meg a személy azonosítóját!')
    write_file = ""
    time_data = []
    for data in list_main:
        if data[2] == person:
            write_file += f'{data[0]}:{data[1]}-' if data[3] == "be" else f'{data[0]}:{data[1]}\n'
    print("7.feladat\n" + write_file)
    for data in list_main:
        if data[2] == person:
            time_data.append(data[0])
            time_data.append(data[1])
    bennevan = False
    if len(time_data)%4 != 0:
        time_data.append("15")
        time_data.append("0")
        bennevan = True
    part_time_data = []
    osszeg = 0
    while time_data:
        for data in range(4):
            part_time_data.append(time_data[data])
        osszeg += passed_time(*part_time_data)
        part_time_data.clear()
        time_data[0:4] = ""
    print(f'8. feladat\nA(z) {person}. személy összesen {osszeg} percet volt bent,'
          f' {"a megfigyelés végén a társalgóban volt." if bennevan else "a megfigyelés végén nem volt a társalgóban."}')
