print("Определение четвертей которые пересекает отрезок заданный двумя точками")
# input block
number = []
stop = 0
dynamicText = ['x для первой', 'y для первой',
               'x для второй', 'y для второй']
for index in range(4):
    while True:
        number.insert(index, input('Введите координату {} точки, либо "e" для выхода: '.format(dynamicText[index])))
        if number[index] != "e":
            try:
                number[index] = int(number[index])
                break
            except:
                try:
                    number[index] = float(number[index])
                    break
                except:
                    print("Вы ввели некоректные данные, попытайтесь снова")
        else:
            stop = 1
            break
    if stop == 1:
        break
# logical and output block
if stop == 0:
    x1 = number[0]
    y1 = number[1]
    x2 = number[2]
    y2 = number[3]
    # comparison position of line
    text2 = "Отрезок"
    if x1 == x2 and y1 == y2:
        text2 = "Нулевой отрезок"
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        print("{} находится в центре координат".format(text2))
    elif y1 == 0 and y2 == 0:
        print("{} находится на оси Х".format(text2))
    elif x1 == 0 and x2 == 0:
        print("{} находится на оси Y".format(text2))
    else:
        # some magic
        if x1 == 0:
            signX1 = int(x2 / abs(x2))
        else:
            signX1 = int(x1 / abs(x1))
        if y1 == 0:
            signY1 = int(y2 / abs(y2))
        else:
            signY1 = int(y1 / abs(y1))
        if x2 == 0:
            signX2 = int(x1 / abs(x1))
        else:
            signX2 = int(x2 / abs(x2))
        if y2 == 0:
            signY2 = int(y1 / abs(y1))
        else:
            signY2 = int(y2 / abs(y2))
        # print("signA({}, {}); signB({}, {})".format(signX1, signY1, signX2, signY2))
        text = "|что-то пошло нетак|"
        if signX1 == signX2 and signY1 == signY2:
            if signX1 == 1 and signY1 == 1:
                text = "в первой"
            elif signX1 == -1 and signY1 == 1:
                text = "во второй"
            elif signX1 == -1 and signY1 == -1:
                text = "в третей"
            else:
                text = "в четвертой"
            print("{} находится {} четверти".format(text2, text))
        elif signX1 == signX2 and signY1 != signY2:
            if signX1 == 1:
                text = "первой и четвертой"
            else:
                text = "второй и третей"
            print("Отрезок находится в смежных {} четвертях".format(text))
        elif signX1 != signX2 and signY1 == signY2:
            if signY1 == 1:
                text = "первой и второй"
            else:
                text = "третей и четвертой"
            print("Отрезок находится в смежных {} четвертях".format(text))
        else:
            if signX1 == signY1:
                text = "первой и третей"
            else:
                text = "второй и четвертой"
            print("Отрезок находится в диагональных {} четвертях".format(text))
print("Готово!")

