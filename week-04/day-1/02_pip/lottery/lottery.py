# Create a method that returns the five most frequent lottery number in a pretty table format
from prettytable import PrettyTable

def five_most_frequent():
    lottery = open('otos.csv', 'r')
    lottery_data = lottery.read()
    lottery_data = lottery_data.split('\n')
    repository = []
    result = {1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0]}
    counted_number= 0
    j = 1

    for i in lottery_data:
        i = i.split(';')[-5:]
        repository += i
    repository.sort()

    for i in range(1, 90):
        i = str(i)
        j = 1
        counted_number = repository.count(i)
        print (counted_number)
        while j <= 5:
            if counted_number > result[j][1]:
                result[j] = [i, counted_number]
                break
            j += 1
    print(result)

    table = PrettyTable(['number', 'frequency'])
    # table.padding_width = 1 # One space between column edges and contents (default)
    table.add_row([result[1][0],result[1][1]])
    table.add_row([result[2][0],result[2][1]])
    table.add_row([result[3][0],result[3][1]])
    table.add_row([result[4][0],result[4][1]])
    table.add_row([result[5][0],result[5][1]])

    print(table)
    return (table)
    lottery.close()

five_most_frequent()
