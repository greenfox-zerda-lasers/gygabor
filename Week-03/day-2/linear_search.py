# expected output: 2

def linear_search(list, num):
    j = -1
    n = 0
    for i in list:

        if i == num:
            j = n

        n += 1

    return j


k = linear_search([4, 5, 6], 6)
print(k)
