from math import sin
 
x = int(input("x="))
if x > 0:
    y = sin(x)**2
else:
    y = 1 - (2 * sin(x * x))
print(y)
