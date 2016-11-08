# Create a method that returns the five most frequent lottery number in a pretty table format
# from prettytable import PrettyTable

def five_most_frequent():
    lott = open('otos.csv', 'r')
    repo = []
    result = {}
    num = ''
    count = 0
    for i in lott:
        i = i[:-1]
        i = i.split(';')[-1:-6:-1]
        repo += i
    repo.sort()

    for i in range(len(repo)):
        while repo[i] == repo[i+1]:
            count += 1

        result[i] = count
    print(result)
    print (repo)
    print (len(repo))
    lott.close()
    # return (table)

five_most_frequent()
