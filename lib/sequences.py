#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list=[]
    if length == 0:
        print(fibonacci_list)
        return fibonacci_list
    if length == 1:
        fibonacci_list.append(0)
        print(fibonacci_list)
        return fibonacci_list
    current=1
    previous=0
    fibonacci_list.append(previous)
    fibonacci_list.append(current)
    while len(fibonacci_list) < length:
        next= current + previous
        fibonacci_list.append(next)
        temp= current
        current= next
        previous= temp
    print(fibonacci_list)
print_fibonacci(10)



    
