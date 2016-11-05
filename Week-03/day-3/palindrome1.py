def palindrome(string):
    string += string[::-1]
    return string

pali = 'wert'
i = palindrome(pali)
print(i)
