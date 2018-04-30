from random import randint


# функция слияния двух списков со сменой порядка сортирования
# принимает два отсортированых по убыванию списка и возвращает новый отсортированый по возрастанию
def merge(first, second):
    return [first.pop() if (first and second and first[-1] < second[-1]) or (first and not second) else second.pop()
            for _ in range(len(first) + len(second))]


# функция слияния двух списков
# принимает два отсортированых по убыванию списка и возвращает новый отсортированый по убыванию
def inv_merge(first, second):
    return [first.pop() if (first and second and first[-1] < second[-1]) or (first and not second) else second.pop()
            for _ in range(len(first) + len(second))][::-1]


# функция сортировки списка аогоритмом слияния
# принимает несортированый список и возвращает новый отсортированый по убыванию
def m_sort(list_):
    return inv_merge(m_sort(list_[len(list_)//2:]), m_sort(list_[:len(list_)//2])) if len(list_) > 1 else list_


# функция генерации отсортированого списка с рандомных чисел
# принимает длину списка, нижнюю и верхнюю граници генерации случайних чисел
# возвращает список отсортированый по убыванию
def list_gen(len_, start, end):
    return m_sort([randint(start, end) for _ in range(len_)])


def main():
    list1 = list_gen(10, 0, 1000)
    list2 = list_gen(15, 0, 2000)
    print(list1)
    print(list2)
    print(merge(list1, list2))


main()
