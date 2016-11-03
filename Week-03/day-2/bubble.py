
def bubble_sort(numb):
    for i in range(0, len(numb)-1):
        for j in range(0, len(numb)-1-i):
            if numb[j] > numb[j+1]:
                numb[j], numb[j+1] = numb[j+1], numb[j]
    return numb

l = bubble_sort([4,5,6,12,33,8])
print(l)
