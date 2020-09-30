import collections

lis = [1, 2, 3, 4, 5]
for i in range(len(lis)):
    print(lis[i] * lis[i])

print([i * i for i in lis])
lis.reverse()
print(lis)

lista = [1, 2, 3, 4, 5]
b = [a ** 2 if a % 2 == 0 else a ** 3
     for a in lista]
print(lista)
print(b)

listb = [5, 4, 3, 6, 7, 1, 7, 1]
listc = [1, 2, 5, 1]

listd = [(listb[i], listc[i]) for i in range(min(len(listb), len(listc)))]
listd = list(zip(listb, listd))
print('****************************')

List = [1, 1, 3, 3, 3, 4, 4, 2, 2, 3, 2, 2, 1, 1, 3]

def most_frequent(List):
    return max(set(List), key=List.count)


print(most_frequent(List))
print('****************************')

chisla = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
counter = collections.Counter(chisla)
print(counter)
print(counter.values())
print(counter.keys())
print(counter.most_common(3))

def kek(string, dup):
    return string*dup

print(kek("ku", 3))

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

nums = [4, 5, 6, 7, 8, 9, 0]
print(nums)

shift(nums, -1)
print(nums)

shift(nums, 2)
print(nums)
