number = input('Введите число от 3 до 20: ')
if (int(number) < 3 ):
    print(f'Число', number, '< 3, принимаем 3')
    number = 3
if (int(number) > 20 ):
    print(f'Число', number, '> 20 принимаем 20')
    number = 20
result = []
for i in range(1, int(number)):
    for j in range(i + 1 , int(number)):
        if int(number) % (i + j) == 0:
            result.append(str(i) + '+' + str(j))
print(*result)
