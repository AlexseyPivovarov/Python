def merge(first, second):
    return [first.pop() if (first and second and first[-1] > second[-1]) or (first and not second) else second.pop()
            for _ in range(len(first) + len(second))][::-1]


def m_sort(list_):
    return merge(m_sort(list_[len(list_)//2:]), m_sort(list_[:len(list_)//2])) if len(list_) > 1 else list_


