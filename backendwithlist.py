import random
from itertools import product
import time
from typing import List

list_addition3x_start = []
list_addition2x_start = []
list_subtraction3x_start = []
list_subtraction2x_start = []
list_multiplication3x_start = []
list_multiplication2x_start = []
list_multiplication1x_start = []
list_division3x_start = []
list_division2x_start = []
arithmetic_mean_addition3x = []
arithmetic_mean_addition2x = []
arithmetic_mean_substraction3x = []
arithmetic_mean_substraction2x = []
arithmetic_mean_subtraction3x = []
arithmetic_mean_subtraction2x = []
arithmetic_mean_multiplication3x = []
arithmetic_mean_multiplication2 = []
arithmetic_mean_division3x = []

arithmetic_mean_division2x = []
##def arithmetic_mean(lst):  # пример вычисления среднего арифметического
##    s = 0
##    for i in lst:
##        s += i
##    i = s / len(lst)

def main(r1, r2, r3, r4, action, summ, hmistake):
    global list_addition3x_start
    global arithmetic_mean_addition3x
    m = 0  # number of correct answers
    error = 0
    arithmetic_mean_list = [0]
    right = 0
    while right <= m:

        tm1 = time.time()
        first = random.randint(r1, r2)
        second = random.randint(r3, r4)
        if action == '+':
            n = first + second
            print(first, '+', second)
        elif action == '-':
            n= first - second
            print(first, '-', second)
        elif action == '*':
            n = first * second 
            print(first, '*', second)
        elif action == '/':
            n = first / second
            print(first, '/', second)
        answer = int(input())

        if answer == n:

            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            list_addition3x_start.append(timenumber)

        else:

            error += 1
            m += hmistake
            print('Осталось', m + hmistake, ' примеров')

        if right == m:

            break

    s = 0

    for i in list_addition3x_start:
        s += i
    i = s / len(list_addition3x_start)

    arithmetic_mean_addition3x.append(i)
    print(list_addition3x_start)
    print(arithmetic_mean_addition3x)



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


def plusandminus(examples, n1, n2, n3, n4):
    tm1 = time.time()
    examples = 50
    a = 0   
    while True:
        tm1 = time.time()
        b = random.randint(n1, n2)
        c = random.randint(n3, n4)
        if b >= c:
            continue
        first = random.randint(b, c)
        second = random.randint(b, c)
        third =  random.randint(b, c)
        if third >= first + second:
            continue 
        n = first + second - third
        print(first, '+', second, '-', third)
        print(n)
        answer = int(input())   
        if answer == n:
            print('sidnjdn')
        else:
            a += 1
        if examples == 0:
            tm2 = time.time()
            break

    s = 0

    for i in list_addition3x_start:
        s += i
    i = s / len(list_addition3x_start)

    arithmetic_mean_addition3x.append(i)
    print(list_addition3x_start)
    print(arithmetic_mean_addition3x)


        
def multX(n1, n2, mestake, amount, x): #умножение на определенное число
    mest = 0
    list = []
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
            a = '{} {} {} {} {}, {}, {}, {}'.format(number, '*', x, '=', n,"Введенный ответ: {}".format(answer), 'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ правильный')
            list.append(a)
            time1.append(timenumber)
        else:
    
            mest += 1
            amount += mestake
            print("Осталось примеров: ", amount, '\n Допущено ошибок: ', mest)
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            a = '{} {} {} {} {}, {}, {}, {}'.format(number, '*', x, '=', n, 'Введенный ответ: {}'.format(answer),'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ неправильный')
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

multX(1, 10, 1, 3, 5)

def a1000a(n1, n2, n3, mestake, amount): #пример типа a - (n3 - a)

    mest = 0
    list = []
    time1 = []
    
    while True:
        tm1 = time.time()
        number = random.randint(n1, n2)
        if number <= n3 - number:
        
            continue
        
        n = number - (n3 - number)
        print(number, ' - ', '( ', n3, ' - ', number, ' ) ', n)
        answer = int(input())

        if  answer == n:
        
            tm2 = time.time()
            amount -= 1
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            a = '{} {} {} {} {} {} {} {} {}, {}, {}, {}'.format(number, '-', '(', n3, '-', number, ')', '=', n,'введеный ответ: {}'.format(answer), 'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ правильный')
            list.append(a)
            time1.append(timenumber)
            print('Верно! Осталось примеров: ', amount)
        
        else:
            tm2 = time.time()
            timenumber = tm2 - tm1
            timenumber = int(timenumber)
            mest += 1
            amount += mestake
            print("Неверно. Осталось примеров: ", amount, '\n Допущено ошибок: ', mest)
            a = '{} {} {} {} {} {} {} {} {}, {}, {}, {}'.format(number, '-', '(', n3, '-', number, ')', '=', n,'введеный ответ: {}'.format(answer), 'Время решения: {} {}'.format(timenumber, 'секунд'), 'Ответ неверен') 
            list.append(a)
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


#a1000a(100, 999, 1000, 2, 5)

