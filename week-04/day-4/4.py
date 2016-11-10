# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def powerN(number1, number2):
    if number2 <= 1:
        return number1
    else:
        return number1 * powerN(number1, number2 - 1)

i = powerN(4, 0)
print(i)
