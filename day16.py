def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a // gcd(a, b)) * b 


x, y = 4, 6
print(lcm(x, y))
