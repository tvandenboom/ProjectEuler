n = 600851475143

factor = 2
while (factor < n):
    while (n % factor == 0):
        n = int(n/factor)
    factor += 1.
print(int(factor))
