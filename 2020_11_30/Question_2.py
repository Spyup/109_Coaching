import os
while True:
    try:
        k = input()
        a, b = k.split()
        index = 0
        flag = True
        for i in range(len(a)):
            index_old = index
            for j in range(index, len(b)):
                if (a[i] == b[j] and j > index):
                    index = j
                    break
            if (index == index_old):
                flag = False
                break
        print(flag)

    except:
        os._exit(0)
