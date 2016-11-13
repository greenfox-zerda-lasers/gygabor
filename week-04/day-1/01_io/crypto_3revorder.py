# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    t = open('texts/reversed_zen_order.txt')

    result = ''

    for i in t:

        result = i + result

    t.close()
    return result
