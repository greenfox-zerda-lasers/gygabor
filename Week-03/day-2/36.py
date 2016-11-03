numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list


def reverse(list):
    reversed = []
    j = len(list) - 1
    for i in list:

        reversed.append(list[j])
        j -= 1

    return reversed

numbers = reverse(numbers)
print(numbers)
