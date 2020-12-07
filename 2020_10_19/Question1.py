while True:
    try:
        q = input("請輸入三邊長：")
        x, y, z = q.split()
        x = int(x)
        y = int(y)
        z = int(z)
        print("x:", x, "y:", y, "z:", z)
        # 邊長一
        if x + y > z:
            leng1 = True
        else:
            leng1 = False
        # 邊長二
        if x + z > y:
            leng2 = True
        else:
            leng2 = False
        # 邊長三
        if y + z > x:
            leng3 = True
        else:
            leng3 = False
        # 判斷
        if leng1 & leng2 & leng3:
            print("可以")
        else:
            print("不可以")
    except:
        break
