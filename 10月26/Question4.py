import math


def prime(a):
    # math.ceil 是無條件進位
    # math.sqrt 是開根號
    # 因為因數必為對應，所以只須找一半的數字就好
    for i in range(2, int(math.ceil(math.sqrt(a))), 1):
        if a % i == 0:
            return False
    return True


a = int(input("Enter a positive integer (>1) :"))
list_f = []
i = 2
while i <= a:
    if a % i == 0 and prime(i):
        list_f.append(i)
    i += 1
print(list_f)
