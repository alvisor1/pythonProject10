while True:
    finish = int(input('Для выхода напишите 0, для продолжения - любую цифру: '))
    if finish == 0:
        break
    a = float(input('1 число: '))
    oper = input('Выберите операцию +-/*: ')
    b = float(input('2 число: '))
    if oper == '+':
        def my_calc(a,b):
            return a+b
        print(my_calc(a,b))
    elif oper == '-':
        def my_calc(a,b):
            return a-b
        print(my_calc(a,b))
    elif oper == '*':
        def my_calc(a,b):
            return a*b
        print(my_calc(a,b))
    elif oper == '/' and b != 0:
        def my_calc(a,b):
            return a/b
        print(my_calc(a,b))
    elif b == 0:
        print('Нельзя делить на ноль!')
    elif oper != '+' and oper != '-' and oper != '*' and oper != '/':
        print('Введите правильное значение!')