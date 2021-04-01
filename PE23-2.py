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
sumbundant_list = []

total = 0
stop_at = 28123

for i in range(1,stop_at+1):
    # if (any(i-n in abundant_list for n in abundant_list)):
    #     total += 0
    # else:
    #     print(i)
    #     total += i

    if (sum(divisors(i)[0:-1]) > i):
        abundant_list.append(i)

#print(len(abundant_list))

for i in range(0,len(abundant_list)):
    for j in range(i,len(abundant_list)):
        if (abundant_list[i]+abundant_list[j] not in sumbundant_list and abundant_list[i]+abundant_list[j] <= stop_at):
            sumbundant_list.append(abundant_list[i]+abundant_list[j])

total = stop_at*(stop_at+1)/2 - sum(sumbundant_list)

#print(abundant_list)
#print(sumbundant_list)
print(total)
