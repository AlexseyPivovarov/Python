def coros(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        next(a)
        return a
    return wrapper


@coros
def dialog():

    sey = {
        "hi": "Вас приветствет телефонная книга версии 1.0!!!",
        "help": "Для вызова данной справки введите '/п'\n"
                "Для выхода из приложения - '/в'\n"
                "Для смены языка - '/я'\n"
                "Для просмотра всей книги - '/т'\n"
                "Для поиска либо создания нового контакта введите ключевые слова через пробел\n"
                "Режим редактирования станет доступен если результатом поиска будет единый контакт",
        "enter": "Ваши действия: ",
        "exit": "Всего доброго!",
        "name": "Имя  ",
        "tel ": "Тел  ",
        "mail": "Почта",
    }
    key = yield
    while True:
        key = yield sey[key]


f = dialog()
res = f.send("hi")
print(res)
res = f.send("help")
print(res)
res = f.send("hi")
print(res)