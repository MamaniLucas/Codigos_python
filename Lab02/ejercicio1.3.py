

lst = [i for i in range(1, 100000+1)]
print(lst)










list2 = ["Hey", 20, 14, "Look", "An Example List"]


def total_elements(list):
    count = 0
    for element in list:
        count += 1
    return count


print("The total number of elements in the list: ", total_elements(list2))


def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)


print(createList(10))
