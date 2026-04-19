def osszeg_counter(array):
    output = 0
    set_array = set(array)
    for product in array:
        if product in set_array:
            if array.count(product) == 1:
                output += 500
            elif array.count(product) == 2:
                output += 950
            else:
                output += 950 + 400 * (array.count(product) - 2)
            set_array.remove(product)
    return output
def ertek(input):
    if input == 1:
        return 500
    elif input == 2:
        return 500 + 450
    else:
        return 500 + 450 + 400 * (input - 2)
with open('penztar.txt', 'r') as in_file:
    list_products = in_file.read().replace('\n', "  ").split(' F  ')[0:-1]
    for i in range(len(list_products)):
        list_products[i] = list_products[i].strip().split("  ")
print(f'2. feladat\nA fizetések száma: {len(list_products)}\n') #2.feladat, fizetések száma
print(f'2. feladat\nAz első vásárló {len(list_products[0])} darab árucikket vásárolt.\n')
sorszam = int(input('4. feladat\nAdja meg egy vásárlás sorszámát!'))
arucikk = input('Adja meg egy árucikk nevét!')
darab = int(input('Adja meg a vásárolt darabszámot!'))
db, first = 0, False
for i, product in enumerate(list_products):
    if arucikk in product:
        if not first:
            first_buy, first = i, True
        last_buy = i
        db += 1
print(f'\n5. feladat\nAz első vásárlás sorszáma: {first_buy + 1}')
print(f'Az utolsó vásárlás sorszáma: {last_buy + 1}')
print(f'{db} vásárlás során vettek belőle.\n')
print(f'6. feladat\n{darab} darab vételekor fizetendő: {ertek(darab)}\n\n7. feladat')
list_products_copy = list_products[sorszam - 1]
for product in set(list_products_copy):
        print(f'{list_products_copy.count(product)} {product}')
with open('osszeg.txt', 'w') as out_file:
    for i, product in enumerate(list_products, start=1):
        out_file.writelines(f'{i}: {osszeg_counter(product)}\n')



















