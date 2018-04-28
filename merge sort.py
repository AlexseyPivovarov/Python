def merge_sort(list_):
    print("Splitting ", list_)
    if len(list_) > 1:
        mid = len(list_) // 2
        left_half = list_[:mid]
        right_half = list_[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_[k] = left_half[i]
                i = i + 1
            else:
                list_[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            list_[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            list_[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging ", list_)


test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(test)
print(test)
