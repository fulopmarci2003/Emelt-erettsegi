def helyreallit(list_cod):
    output = ''
    for tup_alpha in zip(*list_cod):
        if any((word.isalnum() or word.isspace() or word == '/') for word in tup_alpha):
            for alpha in tup_alpha:
                if alpha.isalnum() or alpha.isspace() or alpha == '/':
                    output += alpha
                    break
        elif all(word == '#' for word in tup_alpha):
            output += '#'
        elif '$' in tup_alpha:
            output += '$' * (90 - len(output))
    return output
with open('veetel.txt', 'r', encoding='utf-8') as in_file:
    list_main = []
    file = list(map(int, in_file.readline().split()))
    file.append(in_file.readline()[0:-1])
    while file[0] != '':
        list_main.append(file)
        file = list(map(int, in_file.readline().split()))
        file.append(in_file.readline()[0:-1])
print(f'2. feladat\nAz első üzenet rögzítője: {list_main[0][1]}\nAz utolsó üzenet rögzítője: {list_main[-1][1]}\n\n3.feladat')
for data in list_main:
    if 'farkas' in data[2]:
        print(f'{data[0]}.nap {data[1]}. rádióamatőr')
for days in zip(*list_main):
    break
print('\n4.feladat')
for day in set(days):
    print(f'{day}.nap: {days.count(day)} rádióamatőr')
list_cod = []
for i in set(days):
    for data in list_main:
        if data[0] == i:
            list_cod.append(data[2])
    print(helyreallit(list_cod))
    list_cod.clear()




