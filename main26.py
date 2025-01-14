n = int(input("Введите число: "))
r = 0
r = n

s = 0

while (n != 0):
    s = s+(n % 10)
    n = n//10
print(s)

if s % r == 0:
    print('кратно')
else:
    print('не а')
