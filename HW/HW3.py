# Выполнить циклический сдвиг в списке целых чисел на указанное число шагов. Сдвиг также должен быть кольцевым,
# то есть элемент, вышедший за пределы списка, должен появляться с другого его конца.
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst

print(shift([4, 5, 6, 7, 8, 9, 0], -2))


# напишите функцию, которая на вход принимает список и проверяет, имеют ли одинаковую разницу все соседние элементы,
# возвращает True если разница для всех одинакова, иначе False
def has_equal_diff(array):
    diff = array[0] - array[1]
    for i in range(1, len(array)-1):
        if array[i] - array[i+1] != diff:
            return False
    return True

print(has_equal_diff([5, 10, 15, 20, 25]))


#На вход два списка, нужно вернуть список, который состоит из элементов, общих для этих двух списков.
def intersection(a, b, newtype):
    for i in a:
        for j in b:
            if i == j:
                newtype.append(i)
                break
    # return list(set(newtype))         для удаления повторений
    return newtype

print(intersection([1, 3, 1, 2, 3, 5], [2, 1, 1, 4, 5, 13, 1], []))
