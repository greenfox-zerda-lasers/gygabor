# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def changexy(text):

    if text == '':
        return text
    elif text[0] == 'x':
        return 'y' + changexy(text[1:])
    else:
        return text[0] + changexy(text[1:])

i = changexy('xxxxxtetxxxxxgdfdshgxxxxx')
print(i)
