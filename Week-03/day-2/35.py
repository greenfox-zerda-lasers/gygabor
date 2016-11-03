# create a function that returns it's input factorial

def factor(number):
    result = 0
    for i in range(number):
        result = number * i
        i += 1
    return result

j = factor(3)
print(j)
