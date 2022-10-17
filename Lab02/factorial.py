#factorial function memeoria reservad apara la ejecucion del programa 

from timeit import default_timer as timer

start = timer()
def factorial(num):
    
    if num <0:
        print("uiou")
    elif num == 0:
       return 1
    else:
        fact =1
        while (num > 1):
            fact *= num 
            num -= 1
        return fact

num = 2100
print(factorial(num))


end = timer()
delay = end-start
print("> Time {}".format(delay))
