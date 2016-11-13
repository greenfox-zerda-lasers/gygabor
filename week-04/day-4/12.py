# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def add_up(numbers):
    print(numbers)

    if len(numbers) == 0:
        return 0

    elif type(numbers[0]) == list:
        return add_up(numbers[0]) + add_up(numbers[1:])
    else:
        return numbers[0] + add_up(numbers[1:])

i = add_up([1, 2, [3, 4], 1, [1, [2, 4]]])
print(i)
