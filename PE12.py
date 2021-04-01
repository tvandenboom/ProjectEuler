def divisors(n):
    divisors = []
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            divisors.append(i)
    num_divn = len(divisors)
    for j in range(1,num_divn+1):
        divisors.append(int(n/divisors[num_divn-j]))
    return divisors

n = 1

while (len(divisors(n*(n+1)/2)) < 500):
    n += 1

print(n*(n+1)/2)
