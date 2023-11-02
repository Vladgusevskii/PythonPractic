# --coding: utf-8 --
print('Курс Основы программирования начался')

# --coding: utf-8 --
a = 16823
b = 12302
c = 3092
print((a * b) % c)

# --coding: utf-8 --
age = int(input('Введите возраст'))
name = input('введите имя')
r = 16 - age
if age >= 16 and age < 75 and name != 'Иван':
    print('Поздравляем вы поступили во ВГУИТ')
elif age > 0 and age < 16:
    print(f'Сначала нужно окончить школу,тебе еще учиться {r} лет')
else:
    print('недействительный возраст')

# --coding: utf-8 --
seconds = int(input('Введите число секунд: '))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = seconds % 86400 % 3600 // 60
second = seconds % 86400 % 3600 % 60
print(f'Дни: {days}\nЧасы: {hours} \nМинуты: {minutes}\nСекунды: {second}')

# --coding: utf-8 --
n = int(input('Введите число: '))
print(n + n ** 2 + n ** 3 + n ** 4 + n ** 5)

# --coding: utf-8 --
x = input('Введите x: ')
y = input('Введите y: ')
x,y = y,x
print(x,y)

# --coding: utf-8 --
number = int(input('Введите ваше число: '))
if number % 2 == 0:
    print ('Ваше число четное')
else:
    print ('Ваше число нечетное')

# --coding: utf-8 --
name = input('Ваши фамилия, имя?: ')
age = input('Сколько вам лет?: ')
place = input('Где вы живёте?: ')
print(f'Фамилия и имя {name}')
print(f'Ваш возраст: {age}')
print(f'Вы живете в {place}')