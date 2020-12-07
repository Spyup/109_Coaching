# 建表
list_word = ['one', 'two', 'three']
# 連續輸入迴圈
while True:
    try:
        a = int(input())
        while a > 0:
            b = input()
            for i in range(3):
                ac = 0
                # 取出list_word中的一個字串，例如one整個字串
                k = list_word[i]
                # 只執行字串長度一樣的，可省下一點點時間
                if (len(b) == len(k)):
                    for j in range(len(k)):
                        # 如果字母一樣，則紀錄加一
                        if (b[j] == k[j]):
                            ac += 1
                    # 如果紀錄上只錯一個字母以內，則輸出該數字
                    if (ac >= len(k)-1):
                        ac_word = i
            print(ac_word + 1)
            a -= 1
    except:
        break
