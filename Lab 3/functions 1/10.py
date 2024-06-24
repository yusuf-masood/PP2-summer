def un_wo_set(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

# Test cases
print(un_wo_set([1, 2, 4, 0, 0, 7, 5]))   # [1, 2, 4, 0, 7, 5]
print(un_wo_set([1, 0, 2, 4, 0, 5, 7]))   # [1, 0, 2, 4, 5, 7]
print(un_wo_set([1, 7, 2, 0, 4, 5, 0]))   # [1, 7, 2, 0, 4, 5]
