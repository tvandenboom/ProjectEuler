num = 1
max = 1000
sum = 0
while(num < max):
    if (num % 3 == 0) or (num % 5 == 0):
        sum = sum + num
    num += 1
print(sum)
