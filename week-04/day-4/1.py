# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def count_down(number):
    print(number)
    if number == 1:
        return
    else:
        count_down(number-1)

count_down(5)
