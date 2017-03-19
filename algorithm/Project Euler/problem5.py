# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_number():
    number = 27720
    divider = [13, 16, 17, 19]
    i = 0
    while (i <= 3):
        print (number, divider[i])
        if (number % divider[i] == 0):
            i += 1
        else:
            i = 0
            number += 27720
    return number

num = find_number()
print (num)
