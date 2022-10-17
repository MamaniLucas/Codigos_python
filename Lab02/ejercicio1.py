from timeit import default_timer as timer
n = 100
start = timer()

# Execute n times

if n == 1:
    print("Wrong value")
    print("n=", n)
else:
    for i in range(0, n):
        print("i={}".format(i))



end = timer()
delay = end-start
print("> Time {}".format(delay))