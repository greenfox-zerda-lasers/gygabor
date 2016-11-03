ames = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def shortest(string):
    j = len(string[0])

    for i in range(len(string)):
        if j > len(string[i]):
            j = len(string[i])
            k = string[i]
    return k

h = shortest(ames)
print(h)
