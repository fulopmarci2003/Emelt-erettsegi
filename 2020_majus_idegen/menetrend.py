with open('vonat.txt', 'r', encoding='utf-8') as f:
    menetrend = []
    for sor in f:
        sor = sor.strip().split()
        sor[0:4] = list(map(int, sor[0:4]))
        menetrend.append(sor)

ora = int(input('Óra!'))
perc = int(input('Perc!'))

for i in range(1, 13):
    list_by_vonat = list(filter(lambda x: x[0] == i, menetrend))
    for j in range(len(list_by_vonat) - 1):
        if (list_by_vonat[j][2] * 60 + list_by_vonat[j][3]) <= (ora * 60 + perc) < (list_by_vonat[j + 1][2] * 60 + list_by_vonat[j + 1][3]):
            if list_by_vonat[j][4] == 'I':
                print(f'A(z) {i}. vonat a {list_by_vonat[j][1]}. és a {list_by_vonat[j][1] + 1}. állomás között járt.')
                break
            else:
                print(f'A(z) {i}. vonat a {list_by_vonat[j][1]}. állomáson állt.')
                break

