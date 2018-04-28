
def marge(first, second):
    list_ = []
    i, j = 0, 0
    len1 = len(first)
    len2 = len(second)
    while i < len1 and j < len2:
        if first[i] == second[j]:
            list_.extend([first[i], second[j]])
            i += 1
            j += 1
        elif first[i] < second[j]:
            list_.append(first[i])
            i += 1
        else:
            list_.append(second[j])
            j += 1
    if i < len1:
        list_.extend(first[i:])
    if j < len2:
        list_.extend(second[j:])
    return list_


list1 = [i for i in range(101) if i % 2 == 0]
list2 = [i for i in range(101) if i % 2 != 0]
# list1.insert(-1, 99)
# list2.append(100)
print(list1)
print(list2)
print(marge(list1, list2))

