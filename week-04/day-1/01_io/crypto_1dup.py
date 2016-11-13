# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    string = open("texts/duplicated_chars.txt", 'r')
    text = string.read()
    result = ''
    for i in range(len(text)):
        if text[i] == '\n':
            result += '\n'
        elif i % 2 == 0:
            result += text[i]


    string.close()
    return result
