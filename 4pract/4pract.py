# --coding: utf-8 --
def pro():
    a = int(input('Введите число'))
    b = int(input('Введите число'))
    while a <= b :
        print(a)
        a += 1
    else:
        print('error')

print(pro())

# --coding: utf-8 --
def prof():
    a = int(input('Введите число'))
    b = int(input('Введите число'))
    if a < b:
        for r in range(a, b + 1):
            print(r)
    else:
        for r in range(a, b - 1, -1):
            print(r)

print(prof())

# --coding: utf-8 --
def prima():
    a = int(input('Введите число'))
    b = int(input('Введите число'))
    if a > b:
        for r in range(a, b - 1, -1):
            if r % 2 != 0:
                print(r)
    else:
        print('error')

prima()

# --coding: utf-8 --
def chisl():
    N = int(input('Введите количество чисел'))
    return N
def sum():
    s = 0
    for r in range(chisl()):
        a = int(input('Введите число'))
        s += a
        print(s)

print(sum())

#-- coding: utf-8 --
def main():
    n = int(input('Введите число'))
    s = 0
    for chis in range(1,n+1):
        s += chis**3
        print(s)

main()

#-- coding: utf-8 --
def main():
    n = int(input('Введите число'))
    p = 1
    for chis in range(1,n+1):
        p *= chis
        print(p)

main()

#-- coding: utf-8 --
def main():
    n = int(input('Введите число'))
    s = 1
    r = 0
    for chis in range(1,n+1):
        s *= chis
        r += s
        print(r)

main()

#-- coding: utf-8 --
def nkvd():
    n = int(input('Введите число n: '))
    for z in range(1, n + 1):
        for x in range(1, z + 1):
            print(x, sep='', end='')
        print()
nkvd()

#-- coding: utf-8 --
def main():
    n = int(input('Введите число n: '))
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return sum(fib)
print(main())

#-- coding: utf-8 --
def main():
    n = int(input('Введите число n: '))
    k = int(input('Введите число k: '))
    fib = [0, 1]
    for r in range(2, n + 1):
        fib.append(fib[r - 1] + fib[r - 2])
    return sum(fib[k-1:])
print(main())