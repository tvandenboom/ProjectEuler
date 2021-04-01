(num0,num1) = (1,1)
sum = 0
max = 4000000
while (num1 < max):
    if (num1 % 2 == 0):
        sum = sum + num1
    (num0,num1) = (num1,num0 + num1)

print(sum)
