def fib(n):
    print(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
        

si = fib(8)
print(si)