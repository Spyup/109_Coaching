while True:
    try:
        day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        a = int(input())
        while a > 0:
            m, d = input().split()
            m = int(m)
            d = int(d)
            sum = 0
            for i in range(m-1):
                sum += day[i]
            sum += d
            k = sum % 7
            if (k == 1):
                print("Saturday")
            elif (k == 2):
                print("Sunday")
            elif (k == 3):
                print("Monday")
            elif (k == 4):
                print("Tuesday")
            elif (k == 5):
                print("Wednesday")
            elif (k == 6):
                print("Thursday")
            else:
                print("Friday")
            a -= 1
    except:
        break
