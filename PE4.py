j = 999
while (j > 99):
    pal1 = str(j)
    pal2 = pal1[::-1]
    pal = pal1+pal2
    palint = int(pal)
    for m in range(100,1000):
        if (palint % m == 0 and len(str(int(palint/m))) == 3):
            data = (palint, m, int(palint/m))
            print("%d equals %d times %d" % data)
    else:
        j -= 1
