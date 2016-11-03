def bubble_sort(numb):
    for i in range(0, len(numb)-1):
        for j in range(0, len(numb)-1-i):
            if numb[j] > numb[j+1]:
                numb[j], numb[j+1] = numb[j+1], numb[j]
    return numb

def binary_search(numbers, element):
    a = numbers[0]
    value = False
    l = 0
    m = len(numbers)

    for b in numbers:
        if a > b:
            numbers = bubble_sort(numbers)
            a = b
        else:
            a = b

    print (numbers)

    for k in numbers:
        mid = l + (m - l) // 2
        if element < numbers[mid]:
            m = mid + 1
        elif element > numbers[mid]:
            l = mid
        else:
            value = True
            break

    return(value)

exist = binary_search([4,5,6,12,11,33,8,-1], 8)
print(exist)
