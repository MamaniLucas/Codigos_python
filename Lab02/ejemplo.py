
def permutacion(list, s):
    if list == 1:
        return s
    else:
        return [
            y + x
            for y in permutacion(1, s)
            for x in permutacion(list-1, s)
    
       ]


print(permutacion(1, ["3", "4", "5", "6"]))
print(permutacion(2, ["3", "4", "5", "6"]))
print(permutacion(3, ["3", "4", "5", "6"]))
print(permutacion(4, ["3", "4", "5", "6"]))
