#創建list
score = []

#輸入
for i in range(10) :
    var=int(input())
    score.append(var)

#輸出list第三個元素
print(score[2])

#輸出list中1~6的元素
for i in range(6) :
    if i!=5:
        print(score[i],end="")
    else:
        print(score[i])

#在score第2個及第3個元素之間插入數值
var=int(input())
score.insert(2,var)
print(score)

#刪除score中的第一個元素
score.remove(score[0])
print(score)