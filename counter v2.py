from random import randint
from lib import vocabulary


# Создаю рандомную строку
words = vocabulary[randint(0, len(vocabulary))]
print("Случайное слово:", words)
# Основной алгоритм программы
out = {char: [words.count(char), round(100 / len(words) * words.count(char), 2)] for char in words}
# Вывод результата
[print("{} = {} ({}%)".format(key, out[key][0], out[key][1])) for key in out]
