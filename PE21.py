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

sum_amic = 0

for i in range(2,10000):
    sum_i = sum(divisors(i))-i
    compare = sum(divisors(sum_i))-sum_i
    if (i == compare and i != sum_i):
        sum_amic = sum_amic + i
        print(i)
        print(divisors(i))
        print(sum_i)
        print(divisors(sum_i))

print(sum_amic)
