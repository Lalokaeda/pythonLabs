def fast_pow(a, n):
    if n == 0:
        return 1
    
    if n < 0:
        return 1 / fast_pow(a, -n)
    
    if n % 2 == 0:
        return fast_pow(a * a, n // 2)
    
    return a * fast_pow(a, n - 1)

a, n = map(int, input().split())

result = fast_pow(a, n)
print(result)