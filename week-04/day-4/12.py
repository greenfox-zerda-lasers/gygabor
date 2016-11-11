# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def add_up(numbers):

    if numbers[0] == []:
        return numbers
    elif type(numbers[0]) == list:

        return numbers[0,0] + add_up(numbers[0,1:])
    else:
        return numbers[0] + add_up(numbers[1:])

i = add_up([1, 2, [3, 4], 1, [1, [2, 4]]])
print(i)
