numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function


def summa(numb):
    result = 0
    for i in range(len(numb)):
        result += numb[i]
        i += 1
    return result

j = summa(numbers)
print(j)
