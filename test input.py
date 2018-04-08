# comparison of two numbers
print("comparison of two numbers")
# initialise variables
number = []
# input block
stop = 0
dynamicText = ['first', 'second']
for index in range(2):
    while True:
        number.insert(index, input('enter the {} number for comparison or "e" for exit: '.format(dynamicText[index])))
        if number[index] != "e":
            try:
                number[index] = int(number[index])
                break
            except:
                print("you enter the wrong value, retry please")
        else:
            stop = 1
            break
    if stop == 1:
        break
# output block
if stop == 0:
    if number[0] < number[1]:
        print("The min is {}".format(number[0]))
    elif number[0] > number[1]:
        print("The min is {}".format(number[1]))
    else:
        print("There are equal")
print("Done!")


