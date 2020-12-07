while True:
    try:
        a = int(input())
        # 建換算表，位置上分別是，C，H，O，N
        saw = [12.010, 1.008, 16.000, 14.010]
        while a > 0:
            b = input()
            # 用於計算該字母總數
            sum = [0, 0, 0, 0]
            ans = 0
            # 用於紀錄數字
            k = 0
            for i in range(len(b)):
                if (b[i].isdigit()):
                    k *= 10
                    k += int(b[i])
                else:
                    if (i != 0):
                        if k == 0:
                            k = 1
                        # 去換算各字母有多少個
                        if c == 'C':
                            sum[0] += k
                        elif c == 'H':
                            sum[1] += k
                        elif c == 'O':
                            sum[2] += k
                        else:
                            sum[3] += k
                    k = 0
                    c = b[i]
            # 因為迴圈最後一次不會執行換算，所以要再執行換算
            if k == 0:
                k = 1
            if c == 'C':
                sum[0] += k
            elif c == 'H':
                sum[1] += k
            elif c == 'O':
                sum[2] += k
            else:
                sum[3] += k
            # 計算總數
            for i in range(4):
                ans += (sum[i] * saw[i])
            # 格式化輸出
            print("%.3f" % ans)
            a -= 1
    except:
        break
