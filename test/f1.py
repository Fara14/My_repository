def merge_list(*args):
    a = []
    for val in args:
        if type(val) == list or type(val) == set or type(val) == tuple:
            a.extend(val)
        else:
            a.append(val)
    return a
print(merge_list([0, 0], "nice", {5, 4, 1}, (12, 9), None))
