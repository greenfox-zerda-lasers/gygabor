# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def changexy(text):

    if text == '':
        return text
    else:
        return text[0] + '*' + changexy(text[1:])

i = changexy('textg dfdshgx')
print(i)
