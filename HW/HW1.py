dbase = [
    '+5(4671)849-6225',
    '+394(63)128-1148',
    '535(02)715-68-89',
    '+72(23)661-8520',
    '+194(455)628-2961',
    '092158146777',
    '+862(179)416-6138',
    '+3(2697)794-4711',
    '+98(393)874-4458',
    '+3(632)626-8042',
    '+7611528-9013',
    '+88135130-7172',
    '94(3005)670-58-48',
    '+264925558-7301',
    '58(6929)091-8491',
    '+581(067)254-6659',
    '+4(838)997-1720',
    '+7(163)228-1948',
    '72236618520',
    '967(28)959-4951',
    '+53(2121)207-3793',
    '+80(922)2856718',
    '7121-2173999'
]

# (0) удалить из строк все скобки, дефисы и знаки + (воспользоваться функцией .replace())
myBase = []
for el in dbase:
    myBase.append(el.replace('+', '').replace('(', '').replace(')', '').replace('-', ''))
print(myBase, f"\n")


countryQty = []
maxNum = myBase[0]
minNum = myBase[0]
ruBase = []

# (1) привести базу к виду, где вместо строки будет кортеж из трёх чисел (страна, город/оператор, пользователь)
for el in myBase:
    country = el[:len(el)-10]
    city = el[len(el)-10:len(el)-7]
    user = el[len(el)-7:]

    print(f"{el}{(country, city, user)}")

    countryQty.append(country)

    if len(minNum) > len(el):
        minNum = el
    if len(maxNum) < len(el):
        maxNum = el

    if country == '7':
        ruBase.append(el)

print(f"\nКоличество номеров в базе: {len(myBase)}")
myClearBase = set(myBase)
print(f"Количество номеров в базе без повторений: {len(myClearBase)}\n")

countryQty = set(countryQty)
print(f"Количество стран в базе: {len(countryQty)}\n")

print(f"Самый длинный номер {maxNum} состоит из {len(maxNum)} цифр")
print(f"Самый короткий номер {minNum} состоит из {len(minNum)} цифр\n")

print(f"Российские номера:{ruBase}")
