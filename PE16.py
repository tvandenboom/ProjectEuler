num_str = str(2**1000)

sum = 0
digits = len(num_str)

for i in range(0,digits):
    sum += int(num_str[i])

print(sum)
