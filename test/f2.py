list_to_merge = [[1, 8, 3], [-5, 0], [4], [2, 3, 3]]


def merge_list(list_to_merge):
    a = []
    for el in list_to_merge:
        a.extend(el)
    return a


print(merge_list(list_to_merge))