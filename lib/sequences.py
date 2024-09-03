#!/usr/bin/env python3

def print_fibonacci(length):
     if length == 0:
        print([])
     elif length == 1:
        print([0])
     elif length == 2:
        print([0, 1])
     else:
        fib = [0,1]
        for i in range(length-2):
            fib.append(fib[len(fib)-1] + fib[len(fib)-2])
        print(fib)
    