
# Adds a and b, returns as result
def add(a, b):
    c = a + b
    return c

# Returns the highest value from the three given params
def max_of_three(a, b, c):

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    pool = sorted(pool)
    if len(pool) % 2 == 0:
       j = int(len(pool)/2)
       return (pool[j-1]+ pool[j])/2

    else:
       i = int(len(pool)/2 )
       return pool[i]
# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóíú'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = ''
    for char in hungarian:
        if is_vovel(char):
            teve += char + 'v' + char
        else:
            teve += char

    return teve

print(translate('kata'))
