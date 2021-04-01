def isint(n):
    if (n == int(n)):
        return True
    else:
        return False

for a in range(1,501):
    for b in range(a,1000):
        if (a**2 + b**2 == (1000 - a - b)**2 and isint(1000-a-b) and (1000-a-b > 0)):
            print(a*b*(1000-a-b))
            print(a)
            print(b)
            print(1000-a-b)
