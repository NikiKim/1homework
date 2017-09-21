a = int(input('Введите число:'))
b = int(input('Введите число:'))
znak = raw_input('Введите знак:')

if znak == '+':
result = a + b
print (result)
elif znak == '-':
result = a - b
print (result)
else: 
print('Ошибка')