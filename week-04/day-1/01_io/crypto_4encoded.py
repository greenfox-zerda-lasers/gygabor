# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    t = open(file_name)
    text = t.read()
    char = 0
    result = ''
    for i in text:
        if i == ' ':
            result += ' '
        elif i == '\n':
            result += '\n'
        else:
            char = ord(i)-1
            result += chr(char)
    t.close()
    return result
print(decrypt('texts/encoded_zen_lines.txt'))
