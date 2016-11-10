# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

def digits(number):
    i = number % 10
    j = number / 10
    if number / 10 == 1:
        return j+i
    else:

        return digits(j)+i

i = digits(123)
print(i)
