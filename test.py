from random import randint
from merging import m_sort, invert_merge


def list_generator(len_, start, end):
    return m_sort([randint(start, end) for _ in range(len_)])


def main():
    list1 = list_generator(10, 0, 1000)
    list2 = list_generator(15, 0, 2000)
    print(list1)
    print(list2)
    # print(invert_merge(list1, list2))


main()
