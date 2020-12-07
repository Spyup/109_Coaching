while True:
    a = input()
    if (a == '0'):
        break
    else:
        flag = 0
        for i in a:
            if (i == 'A' or i == 'a'):
                flag += 1
            if (i == 'E' or i == 'e'):
                flag += 1
            if (i == 'I' or i == 'i'):
                flag += 1
            if (i == 'O' or i == 'o'):
                flag += 1
            if (i == 'U' or i == 'u'):
                flag += 1
        if (flag == 5):
            print("True")
        else:
            print("False")
