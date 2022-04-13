def fibo(n):
    # n = 1,2 are base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    return fibo(n-1) + fibo(n-2)

# Dynamic programming

def fibo_dynamic(n):
    arr = [0] * n
    arr[0] = 1
    arr[1] = 2
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i -2]

    return arr[-1]


print(fibo_dynamic(5))
