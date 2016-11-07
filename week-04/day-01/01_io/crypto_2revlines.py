# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    t = open('texts/reversed_zen_lines.txt')

    result = ''

    for i in t:
        i = i[::-1]
        result += i.replace('\n', '')
        result += '\n'

    t.close()
    return result
