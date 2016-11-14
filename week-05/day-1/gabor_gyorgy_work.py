
def anagramm(string1, string2):

    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError('Only string please!')

    string1 = string1.lower()
    string2 = string2.lower()
    i = sorted(string1)
    j = sorted(string2)

    if ' ' in i:
        i.remove(' ')
    elif ' ' in j:
        j.remove(' ')

    if i == j:
        return True
    else:
        return False


def count_letters(string):
    result = {}
    string = string.lower()
    if string.isalpha() == False:
        raise TypeError('Only string please!')

    for i in string:
        j = string.count(i)
        result.update({i : j})

    return result



# print(anagramm('al', 'ma la'))
# print(count_letters('al@%ma'))
