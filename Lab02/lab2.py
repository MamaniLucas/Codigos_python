
from timeit import default_timer as timer

start = timer()


def factorial(n):
    if n == 0:
       return 1
    else:
       return n*factorial(n-1)

print(factorial(1))

print("factorial de", n, "es:", factorial(n))
end = timer()
delay = end-start
print("> Time {}".format(delay))
