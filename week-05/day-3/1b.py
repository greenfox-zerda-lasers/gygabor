# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divide_ten(number):
    # while True:
    try:
        return 10 / number
    except ZeroDivisionError:
        print ( '0 is not allowed' )
    except TypeError:
        print ( 'Number please!')

print(divide_ten('dfs'))
