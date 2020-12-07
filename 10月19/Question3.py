num = 0
list_str = input("輸入：").split()
#list_str = var.split()
print("輸出：")
while num < 4:
    max_str = max(list_str)
    print("{max} ， {len} ".format(max=max_str, len=len(max_str)))
    num += 1
    list_str.remove(max_str)
