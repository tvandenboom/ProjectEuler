import math

num_str = str(math.factorial(100))

sum = 0
digits = len(num_str)

for i in range(0,digits):
    sum += int(num_str[i])

print(sum)
