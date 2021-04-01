def fib():
    a,b = 1,1
    while 1:
        yield a
        a,b = a+b,a

count = 2

for n in fib():
    if (len(str(n)) < 1000):
        count += 1
    else:
        print(n)
        break

print(count)
