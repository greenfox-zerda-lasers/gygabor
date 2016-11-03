numbers = [3, 4, 5, 6, 7, 8]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def filt(numb):
    j = 0
    for i in numb:
        if numb[j] % 2 == 0:
            j += 1
        else:
            numb.pop(j)
            j += 1
    return numb

k = filt(numbers)
print (k)
