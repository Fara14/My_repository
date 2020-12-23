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

    def getIndex(lst):
        imin = lst.index(min(lst))
        imax = lst.index(max(lst))
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


# (18) возвращает строку, в которой удаляются слова, где есть хотя бы одна буква указанная пользователем (*argc)
def f18(*args):
    return

print(f"(18) возвращает строку, в которой удаляются слова, где есть хотя бы одна буква указанная пользователем (*argc)"
      f"\n {f18('In the hole in the ground there lived a hobbit')}\n")
