import math
x1 = int(input("enter the x1 coordinate"))
x2 = int(input("enter the x2 coordinate"))
y1 = int(input("enter the y1 coordinate"))
y2 = int(input("enter the y2 coordinate"))
result = math.sqrt(((y2-y1)**2)+((x2-x1)**2))
print(round(result))
