miles = int(input("Enter number of miles:"))
yards = int(input("Enter number of yards:"))
feet = int(input("Enter number of feet:"))
inches = int(input("Enter number of inches:"))
# 計算inches
total_inches = 63360 * miles + 36 * yards + 12 * feet + inches
# 計算meters
total_meters = int(total_inches / 39.37)
# 計算kilometers
kilometers = int(total_meters / 1000)

total_inches = total_inches - total_meters * 39.37
total_inches = total_inches * 2.54

total_meters = int(total_meters - kilometers * 1000)

print("Metric length:")
print(kilometers, "kilometers")
print(total_meters, "meters")
print("%.1f" % total_inches, "centimeters")
