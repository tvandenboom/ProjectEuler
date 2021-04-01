def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True

i = 1
numprimes = 1

find = 10001

while (numprimes < find):
    i += 2
    if (isprime(i)):
        numprimes += 1



print(i)
