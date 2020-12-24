def remove_duplicates(list_of_lists):
    result = []
    for el in list_of_lists:
        if el not in result:
            result.append(el)
    return result


print(remove_duplicates([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
