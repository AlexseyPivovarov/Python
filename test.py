def counter(text):
    base = {char: [0, 0] for char in text}
    for char in text:
        base[char][0] += 1
        base[char][1] = round(base[char][1] + 100 / len(text), 2)
    return base


if __name__ == '__main__':
    words = input("Наберите текст для обработки: ")
    stat = counter(words)
    print("Текст содержит следующее количевство символов:")
    for key in stat:
        print("{} = {} ({}%)".format(key, stat[key][0], stat[key][1]))
