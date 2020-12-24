# (13) возвращает список размера N, заполненного значениями M
def f13(n, m):
    return [m] * n


print(f"(13) возвращает список размера N, заполненного значениями M\n {f13(6, -1)}\n")


# (14) удаляет все элементы списка с данным значением
def f14(a, d):
    for i in a:
        if i == d:
            a.remove(i)
    return a


print(f"(14) удаляет все элементы списка с данным значением\n {f14([1,2,4,5,4,3,4], 4)}\n")


# (15) меняет местами наименьшую и наибольшую цифру в числе
def f15(n):        # сделал сложно и долго, но главное работает. 100% есть решение лучше, но это все что смог сделать((
    lst = []
    while n > 0:
        lst.append(n % 10)
        n //= 10
    lst.reverse()

    def getIndex(ls):
        imin = lst.index(min(ls))
        imax = lst.index(max(ls))
        if imin > imax:
            return imin, imax
        return imax, imin

    lst[getIndex(lst)[0]], lst[getIndex(lst)[1]] = lst[getIndex(lst)[1]], lst[getIndex(lst)[0]]
    result = int((str(lst)).strip("[]").replace(", ", ""))
    return result


print(f"(15) меняет местами наименьшую и наибольшую цифру в числе\n {f15(45321)}\n")


# (16) проверяет число, если в нем цифры расположены по убыванию. Вернуть True если это так
def f16(n):
    lst = []
    while n > 0:
        lst.append(n % 10)
        n //= 10
    lst.reverse()

    for i in range(len(lst)-1):
        if lst[i] <= lst[i+1]:
            return False
    return True


print(f"(16) проверяет число, если в нем цифры расположены по убыванию. Вернуть True если это так\n {f16(6211)}\n")


# (17) определяет, является ли список симметричным
def f17(lst): return lst == lst[::-1]


print(f"(17) определяет, является ли список симметричным\n {f17([9,8,5,6,8,9])}\n")


def f18(st, *args):
    return [w for w in st.split() if not any(c in args for c in w)]


print(f"(18)возвращает строку, в которой удаляются слова, где есть хотя бы одна буква указанная пользователем (*argc)\n"
      f"{f18('in the hole in the ground there lived a hobbit', 't', 'h', 'r')}\n")


def f19(ip):
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


print(f"(19) проверяет, является ли строка корректной записью IP-адреса. Если да, вернуть True, иначе False\n"
      f"{f19('127.0.0.280')}\n")


def f20(string):
    digits = ""
    for digit in string:
        if digit in "0123456789":
            digits += digit
    return digits


print(f" (20) извлекает из строки все символы, являющиеся цифрами и возвращает эту новую строку\n"
      f"{f20(string='ab = 2 + 278')}\n")


def f21(*args):
    chetnye = []
    nechetnye = []
    for el in args:
        if el % 2 == 0:
            chetnye.append(el)
        else:
            nechetnye.append(el)

    average_ch = sum(chetnye)/len(chetnye)
    average_nech = sum(nechetnye)/len(nechetnye)

    return f"Среднее арифметическое для четных: {average_ch}\n Среднее арифметическое для нечетных: {average_nech}\n"


print(f" (21) принимает множество чисел на вход (*argc) и выводит среднее арифметическое для нечетных чисел \n"
      f"и отдельно среднее арифметическое для четных\n {f21(6, 1, 2, 1)}")


def f22(ls):
    result = []
    for i in range(len(ls)):
        if ls[i] != 0:
            result.append(i)
    return result


print(f" (22) возвращает индексы ненулевых элементов списка\n {f22([1, 2, 0, 0, 4, 0])}\n")


def f23(ls, n):
    return min(ls, key=lambda x: abs(x - n))


print(f" (23) возвращает ближайший элемент к заданному значению списка\n {f23([1, 2, 8, 0, 4, 0], 9)}\n")


def f24(st):
    letters = ['и', 'е', 'а']
    result = ""
    for i in st:
        result += i
        if i in letters:
            result += 'c' + i
    return result


print(f" (24) после каждой гласной добавляет букву -с- и повторяет эту гласную (аса, еса, иси, и т.д.)\n"
      f"{f24('привет, как дела')}\n")


def f25(ls):
    max_three = ls[0] + ls[1] + ls[2]
    numb = 0
    for i in range(len(ls)-2):
        if ls[i] + ls[i+1] + ls[i+2] > max_three:
            max_three = ls[i] + ls[i+1] + ls[i+2]
            numb = i
    return ls[numb:numb+3]


print(f"(25)возвращает три последовательных элемента в списке, сумма которых максимальна\n{f25([1, 2, -5, 1, 4, 2])}\n")


def f27(ls):
    result = []
    max_el = max(ls)
    pr = max_el * 0.1
    for i in ls:
        if max_el - pr <= i <= max_el:
            result.append(i)
    return result


print(f" (27) возвращает количество элементов списка, которые отличны от наибольшего элемента не более чем на 10%/n"
      f"{f27([3, 4, 6, 10, 12, 13])}\n")


def f29(ls1, ls2):
    return ls1 == ls2


print(f" (29) проверяет одинаковы ли 2 списка\n {f29([1, 2, 4], [1, 1, 4])}\n")


def f31(ls):
    return ls[::2]


print(f" (31) выводит все элементы списка с четными индексами\n {f31([1, 2, 8, 8, 5, 10, 11, 0, -1])}\n")


def f54(prices, cart):
    result = 0
    for key in cart:
        for key2 in prices:
            if key == key2:
                result += cart[key] * prices[key2]
    return result


print(f"(54) выводит на экран стоимость вашей покупки в корзине. Цены указываются отдельным словарём.\n"
      f"Отдельный словарь вашей корзины (как в примере)\n"
      f"{f54(prices={'apple': 0.7, 'egg': 0.5, 'cola': 2, 'mango': 5}, cart={'apple': 2, 'egg': 10, 'mango': 3})} р.")
