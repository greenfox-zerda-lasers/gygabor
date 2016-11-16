# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def text_lines(filename):
    try:
        t = open(filename)
        result = t.readlines()
        print (result)
        return len(result)
    except FileNotFoundError:
        return 0

print (text_lines('fil.txt'))
