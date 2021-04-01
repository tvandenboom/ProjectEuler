def divisors(n):
    divisors = []
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            divisors.append(i)
    num_divn = len(divisors)
    for j in range(1,num_divn+1):
        divisors.append(int(n/divisors[num_divn-j]))
    divisors = list(set(divisors))
    divisors.sort()
    return divisors

abundant_list = []

total = 0

for i in range(1,28123):
    if (any(i-n in abundant_list for n in abundant_list)):
        total += 0
    else:
        print(i)
        total += i

    if (sum(divisors(i)[0:-1]) > i):
        abundant_list.append(i)

#print(abundant_list)
print(total)
