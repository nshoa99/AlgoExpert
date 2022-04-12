def fibo(n):
    # n = 1,2 are base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    return fibo(n-2) + fibo(n-1)


print(fibo(5))
