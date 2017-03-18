numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 0
j = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        j += 1
    else:
        k += 1

print ('Number of even numbers: ' + str(j))
print ('Number of odd numbers: ' + str(k))
