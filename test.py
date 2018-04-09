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
# logical block
if stop == 0:
    # preparation for the loop
    x = [number[0], number[2]]
    y = [number[1], number[3]]
    print("Вы ввели А({}, {}); B({}, {})".format(x[0], y[0], x[1], y[1]))
    point = []
    # positioning of points and set it to pointA and pointB
    for index in [0, 1]:
        if x[index] > 0:
            if y[index] > 0:
                point.insert(index, 1)
            elif y[index] < 0:
                point.insert(index, 4)
            else:
                point.insert(index, "+X")
        elif x[index] < 0:
            if y[index] > 0:
                point.insert(index, 2)
            elif y[index] < 0:
                point.insert(index, 3)
            else:
                point.insert(index, "-X")
        else:
            if y[index] > 0:
                point.insert(index, "+Y")
            elif y[index] < 0:
                point.insert(index, "-Y")
            else:
                point.insert(index, 0.0)
    pointA = point[0]
    pointB = point[1]
    x1 = number[0]
    y1 = number[1]
    x2 = number[2]
    y2 = number[3]
    print("pointA = {}, pointB = {}".format(pointA, pointB))
    # comparison position of points
print("Готово!")

