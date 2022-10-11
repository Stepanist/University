N = int(input('Введите номер дня: '))
x=int(N/7)
y=int(N+3-x*7)
print(x)
if y==7:
    y=0
print('Цифра, соответствующая дню недели:',y)