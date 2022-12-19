def summa(a,b):    return a+b
def vychet(a,b):    return a-b
def proiz(a,b):    return a*b
def chast(a,b):    return a/b
def pow(a,b): return a**b
def sqr(a): return a**0.5
from math import factorial
def fact(a): return factorial(a)
while True:
    c = input('Укажите арифметический знак либо 0 для завершения: ')
    if c=='0':
        print('Вычисления окончены')
        break
    a = float(input('Введите число: '))
    if c=='√':
        print(sqr(a))
        continue
    if c=='!':
        a = int(a)
        print(fact(a))
        continue
    b = float(input('Введите ещё одно число: '))
    if c=='+':    print(summa(a,b))
    if c=='-':    print(vychet(a,b))
    if c=='*':    print(proiz(a,b))
    if c=='/':
        try:    print(chast(a,b))
        except ZeroDivisionError:    print('На ноль делить нельзя!!!')
    if c=='^': print(pow(a,b))