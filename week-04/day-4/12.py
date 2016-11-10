# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def add_up(numbers):
    if numbers <= 1:
        return numbers
    else:
        return numbers + add_up(numbers - 1)


i = add_up([1, 2, [3, 4], 1, [1, [2, 4]]])
print(i)
