def union(list1, list2):
    unilist = list1
    for i in list2:
        if i in list1:
            continue
        else:
            unilist.append(i)

    return unilist

k = union([4,5,7,66], [4,1,7,8,9,78,66])
print(k)
