def fib(x):
    if x <= 1:
        return 1
    else:
        return x*fib(x-1)
x=int(input())
print(fib(x))
