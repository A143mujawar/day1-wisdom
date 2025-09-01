import math

def div_count(n):
    c = 0
    r = int(math.isqrt(n))
    for i in range(1, r + 1):
        if n % i == 0:
            if i == n // i:
                c += 1
            else:
                c += 2
    return c


print(div_count(12))
