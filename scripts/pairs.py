def get_pairs(lst, num):
    lst = sorted(lst)
    result = []
    for pos, x in enumerate(lst):
        for z in lst[pos+1:]:
            if x + z == num:
                result.append([x, z])

    return result
