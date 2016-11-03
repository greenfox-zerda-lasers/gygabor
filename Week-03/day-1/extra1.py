j = 0

for i in range(2):
    if j < 5:
        for k in range(5):
            j += 1
            print ('*' * j)
    else:
        for k in range(4):
            j -= 1
            print ('*' * j)
