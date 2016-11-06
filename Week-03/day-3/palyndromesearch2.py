def search_palindromes(string):
    palindromes = []
    finded = ''
    for i in range(len(string)-1):
        if string[i+1] == string[i-1] and not(string[i+1] == string[i]):
            j = 1
            finded = string[i]
            while string[i+j] == string[i-j]:
                finded += string[i+j]
                finded = finded[::-1]
                finded += string[i+j]
                j += 1
                if i+j == len(string):
                    palindromes.append(finded)
                    break
            palindromes.append(finded)
        elif string[i+1] == string[i] and i != len(string)-1:
            j = 1
            finded = string[i+1] + string[i]
            while string[(i+1)+j] == string[i-j]:
                finded += string[(i+1)+j]
                finded = finded[::-1]
                finded += string[(i+1)+j]
                j += 1
                if (i+1)+j == len(string):
                    palindromes.append(finded)
                    break
            palindromes.append(finded)

    return palindromes


output = search_palindromes('jfkdhgjghhhhhh')
print(output)
