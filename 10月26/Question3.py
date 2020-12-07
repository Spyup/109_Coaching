def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, int(a % b))


m = int(input("Enter value of M:"))
n = int(input("Enter value of N:"))
print("Greatest common divisor:", gcd(m, n))
