# create a function that takes a list and returns a new list with all the elements doubled
def double(list):

    for i in list:
        list = list+[i]
    return list

numbers = [1,2,3,4,5]
i = double(numbers)
print(i)
