# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def changexy(text):

    if text == '':
        return text
    elif text[0] == 'x':
        return '' + changexy(text[1:])
    else:
        return text[0] + changexy(text[1:])

i = changexy('textgdfdshgx')
print(i)
