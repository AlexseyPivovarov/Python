from os import system, name
from telephonbook.helpers_ import sey, change_lang, help_, show_oll, search_in_base, lang

cls = "cls" if name == "nt" else "clear"


def none_function(*args):
    return


def mainloop():
    cash_args = "__none__"
    cash_function = none_function
    start = True
    while True:
        if start:  # Вывод приветствия
            system(cls)
            print(sey[lang]["hi"])
            print(sey[lang]["help"])
        data = ""
        while not data or data == "__none__":
            data = input(sey[lang]["enter"])  # Начало итерации цыкла основного алгоритма
        if data == '/в' or data == '/e':  # Выход с программы
            return print(sey[lang]["exit"])
        elif data == '/я' or data == '/l':  # Смена языка
            change_lang()
            cash_function() if cash_args == "__none__" else cash_function(cash_args)
            continue
        start = False  # Скрытие приветствия
        if data == '/п' or data == '/h':  # Вывод справки
            help_()
            cash_function = help_
            cash_args = "__none__"
            continue
        elif data == '/т' or data == '/t':  # Вывод всего справочника
            show_oll()
            cash_function = show_oll
            cash_args = "__none__"
            continue
        result = search_in_base(data.split())  # Поиск по справочнику
        show_oll(result)  # Вывод результата поиска
        cash_function = show_oll
        cash_args = result


if __name__ == '__main__':
    mainloop()

