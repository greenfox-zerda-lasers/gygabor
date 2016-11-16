# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divide_ten():
    # while True:
    #     try:

    number = int(input("Please enter a number: "))
    if number % 10 != 0:
        raise ValueError('Only string please!')

    return (number / 10)
print(divide_ten())
