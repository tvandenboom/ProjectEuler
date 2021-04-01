def sumofpds(n):
    s = 1
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            s += i
            if n//i != i: s += n//i
    return s

def solve():
    A = [i for i in range(2,28124) if sumofpds(i) > i]
    mask = [0] * 28124
    for i in range(len(A)):
        for j in range(i, len(A)):
            s = A[i] + A[j]
            if s < 28124: mask[s] = 1
            else: break
    total = sum([i for i,el in enumerate(mask) if not el])
    print(total)

solve()
