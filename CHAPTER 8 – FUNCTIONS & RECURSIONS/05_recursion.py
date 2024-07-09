def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter a number: "))
print(factorial(n))



def fibonacci(n):
    if(n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))