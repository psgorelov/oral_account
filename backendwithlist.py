import random
from itertools import product
import time
from typing import List


def main(n1, n2, n3, n4, amount, mestake, action): # amount - кол-во примеров; mestake - сколько добавлять за ошибку; action - действие ( +, -, *, /)

    mest = 0
    list1 = []
    time1 = []
    m = 0

    while True:
        tm1 = time.time()
        number1 = random.randint(n1, n2)
        number2 = random.randint(n3, n4)
        if action == '+':
            n = number1 + number2
            print(number1, '+', number2)
        elif action == '-':
            n= number1 - number2
            print(number1, '-', number2)
        elif action == '*':
            n = number1 * number2 
            print(number1, '*', number2)
        elif action == '/':
            n = number1 / number2
            print(number1, '/', number2)
        answer = int(input())

        if answer == n:
        
            m += 1
            tm2 = time.time()
            amount -= 1
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            if timenumber == 0:
                timenumber = 1
            a = '{} {} {} {} {}, {}, {}, {}'.format(number1, '{}'.format(action), number2, '=', n, 'Введенный ответ: {}'.format(answer), 'Время решения: {}'.format(timenumber), 'Ответ правильный')
            list1.append(a)
            time1.append(timenumber)
            print('Осталось примеров: {}'.format(amount))

        else:

            tm2 = time.time()
            mest += 1
            amount += mestake
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            if timenumber == 0:
                timenumber = 1
            a = '{} {} {} {} {}, {}, {}, {}'.format(number1, '{}'.format(action), number2, '=', n, 'Введенный ответ: {}'.format(answer), 'Время решения: {}'.format(timenumber), 'Ответ неправильный')
            list1.append(a)
            time1.append(timenumber)
            print('Ответ неправильный. Осталось примеров: {}'.format(amount))

        if amount == 0:

            print('Все примеры были решены. Ошибок: {}. Всего примеров: {}'.format(mest, m))
            break

    s = 0
    
    for i in time1:
        s += i
    
    i = s / len(time1)
    i = int(i)
    print('Среднее время решения примера: ', i)

    for i in list1:
        print('\n {}'.format(i))


def division3x():  # Деление

    list_division3x_start = []
    time1 = time.time()
    a = 0
    error = 0
    examples = 2
    pairs = [(den, res) for (den, res) in product(range(2, 51), repeat=2) if
             den * res <= 1000]  # подбор рандомных чисел

    for i, (den, res) in enumerate(random.sample(pairs, 15)):
        print("{}) Сколько будет {} / {} = ?".format(i + 1, den * res, den))
        res2 = int(input("Ответ: "))

        if res2 == res:

            examples -= 1
            time2 = time.time()
            timenumber = int(time2 - time1)
            list_division3x_start.append(timenumber)
            print('Вы правы! Осаталось примеров: ', examples)

        else:

            error += 1
            examples += 10
            print('Вы неправы, ответ:', res, "Осталось примеров: ", examples)

        if examples == 0:

            break

    s = 0

    for i in list_division3x_start:
        s += i
    i = s / len(list_division3x_start)
    arithmetic_mean_division3x.append(i)

    print('Значение времени решения каждого примера', list_division3x_start)
    list_division3x_start = []
    print('Среднее значение времени', arithmetic_mean_division3x)


def division2x():  # Деление

    list_division2x_start = []
    global arithmetic_mean_division2x
    time1 = time.time()
    a = 0
    examples = 2
    pairs = [(den, res) for (den, res) in product(range(2, 51), repeat=2) if
             den * res <= 100]  # подбор рандомных чисел

    for i, (den, res) in enumerate(random.sample(pairs, 15)):

        print("{}) Сколько будет {} / {} = ?".format(i + 1, den * res, den))
        res2 = int(input("Ответ: "))

        if res2 == res:

            examples -= 1
            tm2 = time.time()
            timenumber = int(tm2 - time1)
            list_division2x_start.append(timenumber)
            print('Вы правы! Осаталось примеров: ', examples)

        else:

            examples += 10
            print('Вы неправы, ответ:', res, "Осталось примеров: ", examples)

        if examples == 0:

            break

    s = 0

    for i in list_division2x_start:
        s += i
    i = s / len(list_division2x_start)
    arithmetic_mean_division2x.append(i)

    print('Значение времени решения каждого примера', list_division2x_start)
    list_division2x_start = []
    print('Среднее значение времени', arithmetic_mean_division2x)


def manyactions(n1, n2, action1, action2, amount, mestake): #
    
    mest = 0
    list1 = []
    time1 = []

    while True:
       
        tm1 =time.time()
        number1 = random.randint(n1, n2)
        number2 = random.randint(n1, n2)
        number3 = random.randint(n1, n2)
    
        if action1 == '+' and action2 == '-':
    
            n = number1 + number2 - number3
            print('{} + {} - {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} + {} - {}'.format(number1, number2, number3)
        if action1 == '-' and action2 == '+':
            n = number1 - number2 + number3
            print('{} - {} + {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} - {} + {}'.format(number1, number2, number3)
        if action1 == '+' and action2 == '*':
            n = number1 + number2 * number3
            print('{} + {} * {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} + {} * {}'.format(number1, number2, number3)
        if action1 == '+' and action2 == '/':
            n = number1 + number2 / number3
            print('{} + {} / {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} + {} / {}'.format(number1, number2, number3)
        if action1 == '-' and action2 == '*':
            n = number1 - number2 * number3
            print('{} - {} * {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} - {} * {}'.format(number1, number2, number3)
        if action1 == '-' and action2 == '/':
            n = number1 + number2 - number3
            print('{} - {} / {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} - {} / {}'.format(number1, number2, number3)
        if action1 == '*' and action2 == '+':
            n = number1 + number2 - number3
            print('{} * {} / {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} * {} / {}'.format(number1, number2, number3)
        if action1 == '*' and action2 == '-':
            n = number1 + number2 - number3
            print('{} * {} - {}'.format(number1, number2, number3))
            answer = int(input())
            #n1 = '{} * {} - {}'.format(number1, number2, number3)
        if action1 == '*' and action2 == '/':
            n = number1 + number2 - number3
            print('{} * {} / {}'.format(number1, number2, number3))
            answer = int(input())
           # n1 = '{} * {} / {}'.format(number1, number2, number3)

        if answer == n:
        
            tm2 = time.time()
            amount -= 1
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            if timenumber == 0:
                timenumber = 1
            a = '{} {} {} {} {} = {}, {}, {}, {}'.format(number1, action1, number2, action2, number3, n, 'Введенный ответ: {}'.format(answer),  'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ правильный')
            list1.append(a)
            time1.append(timenumber)
            if amount > 0:
                print('Осталось примров: ', amount)

        else:
    
            mest += 1
            amount += mestake
            print('Осталось примеров: {} , \n Допущено ошибок: {}'.format(amount, mest))
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            if timenumber == 0:
                timnumber = 1
            a = '{} = {}, {}, {}, {}'.format(n1, n, 'Введенный ответ: {}'.format(answer),  'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ неправильный')
            list1.append(a)
            time1.append(timenumber)

        if amount == 0:
    
            print('Все примеры решены. Количество допущенных вами ошибок: ', mest)
            break

    s = 0
    for i in time1:
        s += i
    i = s / len(time1)
    i = int(i)
    print('Среднее время решения примера: ', i)

    for i in list1:
        print('\n {}'.format(i))


def multX(n1, n2, mestake, amount, x): #умножение на определенное число
    
    mest = 0
    list1 = []
    time1 = []
    
    while True:
        
        tm1 = time.time()
        number = random.randint(n1, n2)
        print(number, '*', x)
        n = number * x
        answer = int(input())
        
        if answer == n:
            
            tm2 = time.time()
            amount -= 1
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            if timenumber == 0:
                timenumber = 1
            a = '{} {} {} {} {}, {}, {}, {}'.format(number, '*', x, '=', n,"Введенный ответ: {}".format(answer), 'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ правильный')
            list1.append(a)
            time1.append(timenumber)
            print('Осталось примеров: {}'.format(amount))

        else:
    
            mest += 1
            amount += mestake
            print("Осталось примеров: ", amount, '\n Допущено ошибок: ', mest)
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            if timenumber == 0:
                timenumber = 1
            a = '{} {} {} {} {}, {}, {}, {}'.format(number, '*', x, '=', n, 'Введенный ответ: {}'.format(answer),'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ неправильный')
            list1.append(a)
            time1.append(timenumber)
        if amount == 0:
    
            print('Все примеры были решены. Количество допущенных Вами ошибок: ', mest)
            break        
    
    s = 0
    for i in time1:
        s += i
    i = s / len(time1)
    i = int(i)
    print('Среднее время решения примера: ', i)

    for i in list1:
        print('\n {}'.format(i))


def a1000a(n1, n2, n3, mestake, amount): #пример типа a - (n3 - a) n1 и n2 границы возможного числа metake - сколько прибавлять примеров за ошибку amount - количество примеров n3 число из которого вычисялть


    mest = 0
    list = []
    time1 = []
    
    while True:
        tm1 = time.time()
        number = random.randint(n1, n2)
        if number <= n3 - number:
        
            continue
        
        n = number - (n3 - number)
        print(number, ' - ', '( ', n3, ' - ', number, ' ) ')
        answer = int(input())


        if  answer == n:
        
            tm2 = time.time()
            amount -= 1
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            if timenumber == 0:
                timenumber = 1
            a = '{} {} {} {} {} {} {} {} {}, {}, {}, {}'.format(number, '-', '(', n3, '-', number, ')', '=', n,'введеный ответ: {}'.format(answer), 'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ правильный')
            list.append(a)
            time1.append(timenumber)
            print('Верно! Осталось примеров: ', amount)
            
        else:
            
            tm2 = time.time()
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            if timenumber == 0:
                timenumber = 1
            mest += 1
            amount += mestake
            print("Неверно. Осталось примеров: ", amount, '\n Допущено ошибок: ', mest)
            a = '{} {} {} {} {} {} {} {} {}, {}, {}, {}'.format(number, '-', '(', n3, '-', number, ')', '=', n,'введеный ответ: {}'.format(answer), 'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ неправильный') 
            list.append(a)
            time1.append(timenumber)
        if amount == 0:

            print('Все примеры были решены. Количество допущенных Вами ошибок: ', mest)
            break        
    
    
    s = 0
    for i in time1:
        s += i
    i = s / len(time1)
    i = int(i)
    print('Среднее время решения примера: ', i)

    for i in list:
        print('\n {}'.format(i))
    

manyactions(100, 999, '+', '-', 50, 10)
main(100, 1000, 100, 1000, 10, 20, '+')
multX(100, 999, 10, 20, 5)
a1000a(100, 999, 1000, 5, 5)