import os
while True:
    try:
        k = input().split()
        k.remove(k[0])
        k = list(map(int, k))
        diff = []
        flag = True
        for i in range(len(k)):
            diff.append(abs(k[i - 1] - k[i]))
        p = list(range(1, len(k)))
        for i in range(len(diff)):
            for j in range(len(p)):
                if (diff[i] == p[j]):
                    p[j] = 0
        for i in range(len(p)):
            if (p[i] != 0):
                flag = False
                break
        if (flag == True):
            print("It's Jolly")
        else:
            print("It's Not jolly")
    except:
        os._exit(0)
