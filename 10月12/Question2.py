var=input()
num=0
while var!="" :
    num+=1
    var=var.replace(var[0],"",1)
print(num)