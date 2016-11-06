# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def stars(number):
    if number == 1:
        print ('*')
    else:
        space = number - 1

        for i in range(number):
            k = '*' * (i * 2 + 1)
            print (' ' * space + k)
            space -= 1


i = stars(2)
