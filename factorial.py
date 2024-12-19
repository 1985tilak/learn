## recursion function. function calling itself.
## recursive function should always have a a base case along with recursive case. 

def factorial(n):
    if n == 1:  ## this is base case
        return 1 
    return n * factorial(n-1) ## this is recursive case




## iterative approach to find the factorial of a number

def factorial(n):
    result = 1 
    for i in range(1, n+1):  # range(start, stop)  n + 1 will stop at n.  
        result *= i 
    return result

print(factorial(4))