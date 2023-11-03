#-- coding: utf-8 --
#вариант 15
stroka = input('Введите строку')
stroka.split(' ')

def bukva():
    kolvo = 0
    for bet in stroka:
        if bet == 'т':
            kolvo += 1
    print(kolvo)

bukva()