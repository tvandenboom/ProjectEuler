def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True

def divisors(n):
    divisors = []
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            divisors.append(i)
    k = len(divisors)
    for j in range(1,k+1):
        divisors.append(int(n/divisors[k-j]))
    return divisors

x = 600851475143
div = divisors(x)
print(divisors(x))

primediv = []
for i in range(0, len(div)):
    if isprime(div[i]):
        primediv.append(div[i])

print(primediv)
