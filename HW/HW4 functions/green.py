# (1) на вход получает два числа. Верните tuple суммы и произведения данных чисел
def f1(x, y): return x + y, x * y


print(f"(1) на вход получает два числа. Верните tuple суммы и произведения данных чисел\n {f1(4, 10)}\n")


# (2)вычисляет sqrt(x + sqrt(y))
def f2(x, y): return (x + y ** 0.5) ** 0.5


print(f"(2)вычисляет sqrt(x + sqrt(y))\n {f2(5, 16)}\n")


# (3) выводит на экран числа между 1000 и 4250 (оба включены), которые делятся на 5, но не кратны 3
def f3(x, y):
    a = []
    for i in range(x, y + 1):
        if i % 5 == 0 and i % 3 != 0:
            a.append(i)
    return a


print(f"(3) выводит на экран числа между 1000 и 4250 (оба включены), которые делятся на 5, но не кратны 3\n"
      f"{f3(1000, 4250)}\n")


# (4) принимает на вход число. Если оно от 3 до 6 включительно, то уменьшить его на 13. Если оно от 8 до 41, то
# уменьшить на 50.Если оно не более 0 или более 2000, то увеличить в 4 раза. Иначе занулить это число. Вернуть результат
def f4(x):
    if 3 <= x <= 6:
        return x - 13
    elif 8 < x < 41:
        return x - 50
    elif x <= 0 or x > 2000:
        return x * 4
    else:
        return int(x == 0)


print(f"(4) принимает на вход число. Если оно от 3 до 6 включительно, то уменьшить его на 13. Если оно от 8 до 41, то "
      f"уменьшить на 50.\n Если оно не более 0 или более 2000, то увеличить в 4 раза. Иначе занулить это число. "
      f"Вернуть результат\n {f4(2)}\n")


# (5)принимает значение в градусах Цельсия, а выводит температуру  в градусах Фаренгейта
def f5(x): return (9/5) * x + 32


print(f"(5)принимает значение в градусах Цельсия, а выводит температуру  в градусах Фаренгейта\n {f5(0)}\n")


# (6) на вход получает сумму вклада в банк и годовой процент. Вывести на экран сумму вклада через 5 лет
def f6(x, y): return x*(1 + 0.01*y)**5


print(f"(6) на вход получает сумму вклада в банк и годовой процент. Вывести на экран сумму вклада через 5 лет\n "
      f"{f6(200000, 5)}\n")


# (7) получает на вход количество недель, месяцев, лет и выводит количество дней за это время.
def f7(weeks, months, years): return weeks * 7 + months * 30 + years * 360


print(f"(7) получает на вход количество недель, месяцев, лет и выводит количество дней за это время. "
      f"Считать, что в месяце 30 дней.\n {f7(0, 4, 3)}\n")


# (8) возвращает простые множители данного числа
def f8(n):
    mn = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            mn.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        mn.append(n)
    return mn


print(f"(8) возвращает простые множители данного числа\n {f8(40)}\n")


# (9) возвращает все делители данного натурального числа
def f9(num): return [i for i in range(1, num + 1) if num % i == 0]


print(f"(9) возвращает все делители данного натурального числа\n {f9(36)}\n")


# (10) возвращает длину отрезка, когда даны координаты начала и конца
def f10(x1, y1, x2, y2):
    import math
    return math.sqrt(math.sqrt(y2 - y1) + math.sqrt(x2 - x1))


print(f"(10) возвращает длину отрезка, когда даны координаты начала и конца\n {f10(0, 0, 1, 1)}\n")


# (11) выводит все квадраты натуральных чисел, не превосходящие N, в порядке возрастания
def f11(n):
    a = []
    i = 1
    while i ** 2 <= n:
        a.append(i ** 2)
        i += 1
    return a


print(f"(11) выводит все квадраты натуральных чисел, не превосходящие N, в порядке возрастания\n {f11(50)}\n")


# (12) находит сумму элементов в указанном срезе (конец включителен)
def f12(num, x, y): return sum(i for i in num[x:y+1])


print(f"(12) находит сумму элементов в указанном срезе (конец включителен)\n {f12([1, 5, -1, 9, 0, 2], 2, 5)}")
