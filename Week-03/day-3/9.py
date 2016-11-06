# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def stars(number):
    if not(number <= 0):
        for i in range((number)+1):
            sta = ('*' * i)
            print (sta)

i = stars(10)
