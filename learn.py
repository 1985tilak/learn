# linear time O(n)  - increases with the input

def print_items(n):  #n+n = 2n O(2n) O(n)  drop the constant 2 
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

def print_items1(n):  #n*n = n^2  O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j)

def print_items2(n):    # n*n = n^2 O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):   # n  = O(n)  
        print(k)         # O(n^2) + O(n)
                         # O(n^2 + n)
                         # O(n^2) drop the non-dominant n  
print_items2(10)

# Constant time  - doesn't increase with the input

def add_num(n):
    return n+n    #O(1)
