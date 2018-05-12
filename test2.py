words = input("Наберите текст для обработки: ")
out = {char: [words.count(char), round(100 / len(words) * words.count(char), 2)] for char in words}
[print("{} = {} ({}%)".format(key, out[key][0], out[key][1])) for key in out]
