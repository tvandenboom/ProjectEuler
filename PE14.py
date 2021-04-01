def collatz(n):
    collatz = [n]
    while(collatz[-1] != 1):
        if (collatz[-1]%2 == 0):
            collatz.append(collatz[-1]/2)
        else:
            collatz.append(3*collatz[-1]+1)
    return collatz

print(collatz(13))

max_len = 0
output = [1,1]

for i in range(1,1000000):
    if (len(collatz(i)) > max_len):
        max_len = len(collatz(i))
        output = [i,max_len]

print(output)
