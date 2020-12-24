import math


def f(ls, summa, absolut, root):
    if summa and not absolut and not root:
        return sum(ls)

    elif absolut and not summa and not root:
        return [abs(el) for el in ls]

    elif root and not summa and not absolut:
        return [math.sqrt(el) for el in ls]

    elif summa and root and not absolut:
        return sum(math.sqrt(el) for el in ls)

    elif summa and root and absolut:
        return sum(math.sqrt(abs(el)) for el in ls)

    else:
        return ls


print(f([1, -4, 9], True, True, True))
