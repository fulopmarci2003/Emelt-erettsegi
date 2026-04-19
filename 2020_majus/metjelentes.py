def average(n):
    return sum(n) / len(n)
list_data = []
with open("tavirathu13.txt", "r", encoding="utf-8") as fin:
    for file in fin:
        row = file.strip().split()
        ready_dict = {'id': row[0], 'time': (row[1][:2], row[1][2:]), 'wind': (row[2][:3], int(row[2][3:])), 'temp': int(row[3])}
        list_data.append(ready_dict)

cin = input('2. feladat\nAdja meg egy település kódját! Település:')
max_time, max_hour, max_minute = 0, 0, 0
for data in list_data:
    hour, minute = tuple(map(int, data['time']))
    if (hour * 60 + minute) > max_time and data['id'] == cin:
        max_time = hour * 60 + minute
        max_hour, max_minute = hour, minute
print(f'Az utolsó mérési adat a megadott településről {max_hour}:{max_minute}-kor érkezett.')

max_temp, min_temp = 0, 100
for data in list_data:
    if data['temp'] > max_temp:
        max_temp = data['temp']
        max_temp_time = ':'.join(data['time'])
        max_temp_id = data['id']
    if data['temp'] < min_temp:
        min_temp = data['temp']
        min_temp_time = ':'.join(data['time'])
        min_temp_id = data['id']
print('3.feladat')
print(f'A legalacsonyabb hőmérséklet: {min_temp_id} {min_temp_time} {min_temp} fok.')
print(f'A legmagasabb hőmérséklet: {max_temp_id} {max_temp_time} {max_temp} fok.')

print('4. feladat')
list_id_by_wind, list_id_all_wind = [], [],
for data in list_data:
    if data['wind'][0] == '000':
        print(data['id'], ':'.join(data['time']))
        if data['id'] not in list_id_by_wind:
            list_id_by_wind.append(data['id'])
    if data['id'] not in list_id_all_wind:
        list_id_all_wind.append(data['id'])
list_id_all = list_id_all_wind.copy()
for city in list_id_by_wind:
    if city in list_id_all_wind:
        list_id_all_wind.remove(city)
for city in list_id_all_wind:
    print(f'{city} Nem volt szélcsend a mérések idején.')

print('5.feladat')
for city in list_id_all:
    list_temp, list_if_all_mesurement = [], [False, False, False, False]
    max_temp_by_id, min_temp_by_id = 0, 100
    for data in list_data:
        if data['id'] == city:
            if data['time'][0] == '01':
                list_temp.append(data['temp'])
                list_if_all_mesurement[0] = True
            if data['time'][0] == '07':
                list_temp.append(data['temp'])
                list_if_all_mesurement[1] = True
            if data['time'][0] == '13':
                list_temp.append(data['temp'])
                list_if_all_mesurement[2] = True
            if data['time'][0] == '19':
                list_temp.append(data['temp'])
                list_if_all_mesurement[3] = True
            if data['temp'] > max_temp_by_id:
                max_temp_by_id = data['temp']
            if data['temp'] < min_temp_by_id:
                min_temp_by_id = data['temp']
    if all(list_if_all_mesurement):
        print(f'{city} Középhőmérséklet: {average(list_temp):.0f},', end='; ')
        print(f'Hőmérséklet-ingadozás: {max_temp_by_id - min_temp_by_id}')
    else:
        print(city, 'NA', end='; ')
        print(f'Hőmérséklet-ingadozás: {max_temp_by_id - min_temp_by_id}')

for city in list_id_all:
    with open(f'{city}{1}.txt', 'w', encoding='utf-8') as fout:
        fout.writelines(f'{city}\n')
        for data in list_data:
            if data['id'] == city:
                fout.writelines(f'{":".join(data["time"])} {"#" * data["wind"][1]}\n')