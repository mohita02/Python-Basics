import math
amount = int(input("enter the amount"))
rate = int(input("enter the rate of interest"))
time = int(input("enter the time"))
result = amount*(1+rate/100)**time
print(round(result))
