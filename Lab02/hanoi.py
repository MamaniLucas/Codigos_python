
from timeit import default_timer as timer
start = timer()

def hanoi(n):
    if n ==1:
        count = 1
    else:
        count = (2*hanoi(n-1)+1)
    return count

def toH(n, A, B, C):
    if n==1:
        print("Mover disco 1 desde", A, "a", B)
        return
    toH(n-1, A, C, B)
    print("Mover disco", n, "desde", A, "a", B)
    toH(n-1, C, B, A)
def main ():
    n=eval(input("introduzca el número total de discos de la torre de Hanói:"))
    print("{} los discos deben moverse: {} veces".format(n, hanoi(n)))
    toH(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()


end = timer()
delay = end-start
print("> Time {}".format(delay))
