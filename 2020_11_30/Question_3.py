import os
while True:
    try:
        t = int(input())
        for i in range(t):
            k = input().split()
            k = list(map(int, k))
            sum_x = 0
            sum_y = 0
            for j in range(k[2]):
                p = input().split()
                p = list(map(int, p))
                sum_x += p[0]
                sum_y += p[1]
            print("(Street:", sum_x//k[2], "Avenue:", sum_y//k[2], ")")
    except:
        os._exit(0)
