list_str=[]
num=0
for i in range(4):
    var=input()
    list_str.append(var)
while num<4:
    max_str=max(list_str)
    print("{max} ， {len} ".format(max=max_str,len=len(max_str)))
    num+=1
    list_str.remove(max_str)