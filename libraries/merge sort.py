def merge_sort(list_):
    len_ = len(list_)
    if len_ <= 1:
        return
    mid = len_ // 2
    first = list_[mid:]
    second = list_[:mid]
    merge_sort(first)
    merge_sort(second)
    i, j, k = 0, 0, 0
    while j < len(first) and k < len(second):
        if first[j] and second[k]:
            if first[j] < second[k]:
                list_[i] = first[j]
                j += 1
            else:
                list_[i] = second[k]
                k += 1
            i += 1
    while j < len(first):
        list_[i] = first[j]
        j += 1
        i += 1
    while k < len(second):
        list_[i] = second[k]
        k += 1
        i += 1
