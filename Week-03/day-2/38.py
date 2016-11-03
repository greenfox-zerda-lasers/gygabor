numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def smaller(numbs):
    j = numbs[0]
    for i in range (len(numbs)):
        if j > numbs[i]:
            j = numbs[i]

    return j

k = smaller(numbers)
print(k)
