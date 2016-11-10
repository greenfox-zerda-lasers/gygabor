# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def count_down(number):
    if number <= 1:
        return number
    else:
        return number + count_down(number - 1)

i = count_down(2)
print(i)
