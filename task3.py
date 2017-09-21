b = int(input("Введите число: "))
nya = []

for i in range(2, b+1):
for j in nya:
if i % j == 0:
break
else:
nya.append(i)

print (nya)