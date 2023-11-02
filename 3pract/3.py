#-- coding:utf-8--
a = int(input('Введите 1 число'))
b = int(input('Введите 2 число'))
c = int(input('Введите 3 число'))
s = a + b + c
print(s)

#-- coding:utf-8--

def s(a, b):
    a = int(input('Введите 1 сторону'))
    b = int(input('Введите 2 сторону'))
    s = 1 / 2 * a * b
    print('Площадь равна', s)
s(a,b)

#-- coding:utf-8--
n = int(input('Введите минуты'))
hours = n // 60
minute = n % 60
if n >= 1440:
    print('error')
else:
    print(hours,':',minute)

#--coding: utf-8--
def c():
    print(f'Длина всего шнурка: {d}')
a = int(input('расстояние между рядами'))
b = int(input('расстояние между дырочками в ряду'))
l = int(input('длина свободного конца шнурка'))
N = int(input('количество дырочек'))
d = 2 * l + (2 * N - 1) * a + 2 * (N - 1) * b

c()

#--coding: utg-8--
m = int(input('Введите число'))
s = int(input('Введите число'))
d = int(input('Введите число'))
def mensh():
    if m < s and m < d:
        print(m)
    elif s < m and s < d:
        print(s)
    else:
        print(d)

mensh()

#--coding: utf-8--
def chislo():
    a = int(input('Введите номер от 1 до 8'))
    if a >= 1 and a <= 8:
        return a
    else:
        return chislo()
def kletka():
    z = chislo()
    x = chislo()
    c = chislo()
    v = chislo()
    if (z + x) % 2 == (c + v) % 2:
        print('Цвета совпадают')
    else:
        print('Цвета разные')

print(kletka())

#--coding: utf-8--
def year():
    n = int(input('Введите год'))
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print('Високосный')
    else:
        print('Не високосный')

print(year())

#--coding: utf-8--
def chislo():
    a = int(input('Введите число'))
    s = int(input('Введите число'))
    d = int(input('Введите число'))
    if a == s == d:
        print('3')
    elif a == s or a == d or s == d:
        print('2')
    else:
        print('0')

print(chislo())

#--coding: utf-8 --
def kusok():
    n = int(input('Введите число'))
    m = int(input('Введите число'))
    k = int(input('Введите число'))
    if k < n * m and (k % n == 0 or k % m == 0):
        print('Yes')
    else:
        print('No')

print(kusok())