a = int(input("Введите число: "))
b = int(input("Введите число: "))
n = []

for i in range(a,b+1):
if i%5==0:
n.append(i)

print(n)