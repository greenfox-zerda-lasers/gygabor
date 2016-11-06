# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
    #  ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def diamond(number):
    space = number / 2

    if number % 2 == 0:
        maxstar = number - 1
    else:
        maxstar = number

    for i in range(number):
        if i < maxstar / 2:
            k = '*' * (i * 2 + 1)
            print (' ' * space + k)
            space -= 1
        elif i == maxstar / 2:
            k = '*' * (i * 2 + 1)
            print (' ' * space + k)
            space += 1
        else:
            maxstar -= 2
            k = '*' * maxstar
            print (' ' * space + k)
            space += 1


i = diamond(11)
