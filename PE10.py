def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True

i = 3
sumprimes = 2

bound = 2000000

while (i < bound):
    if (isprime(i)):
        sumprimes = sumprimes + i
    i += 2



print(sumprimes)
