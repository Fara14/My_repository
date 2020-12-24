original = [3, 2, 0, -2, -7]
powers = [1/3, 7, 10, -2, 3]


def multi_power(original, powers):
    multi = []
    index = 0
    for o in original:
        multi.append(o**powers[index])
        index += 1
    return multi


print(multi_power(original, powers))