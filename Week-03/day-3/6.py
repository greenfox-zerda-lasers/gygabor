# create a function that takes a list and returns a new list that is reversed
def reverselist(list):
    list.reverse()
    return list

numbers = [1,2,3,4,5]
i = reverselist(numbers)
print(i)
