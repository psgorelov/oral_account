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
arithmetic_mean_division3x = []
arithmetic_mean_division2x = []
##def arithmetic_mean(lst):  # пример вычисления среднего арифметического
##    s = 0
##    for i in lst:
##        s += i
##    i = s / len(lst)




def addition3x():  # сложение трехзначных чисел
    global list_addition3x_start
    global arithmetic_mean_addition3x
    right = 0  # number of correct answers
    m = 50
    error = 0
    arithmetic_mean_list = [0]
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(1, 9)
        second = random.randint(1, 9)
        n = fisrt + second
        print(fisrt, '+', second)
        answer = int(input())
        if right == m:
            break
        if answer == n:
            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            list_addition3x_start.append(timenumber)
        else:
            error += 1
            m += 10
            print('Осталось', m - right, ' примеров')
        if right == m:

            break
    s = 0

    for i in list_addition3x_start:
        s += i
    i = s / len(list_addition3x_start)

    arithmetic_mean_addition3x.append(i)
    print(list_addition3x_start)
    print(arithmetic_mean_addition3x)




def addition2x():  # Cложение 2-х значных чисел ГОТОВО
    global list_addition2x_start
    global arithmetic_mean_addition2x

    right = 0  # number of correct answers
    m = 50
    error = 0

    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(10, 99)
        second = random.randint(10, 99)
        n = fisrt + second
        print(fisrt, '+', second)
        answer = int(input())
        if right == m:

            break

        if answer == n:

            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            list_addition2x_start.append(timenumber)

        else:

            error += 1
            m += 10
            print('Осталось', m - right, ' примеров')

        if right == m:

            break

    s = 0

    for i in list_addition2x_start:
        s += i
    i = s / len(list_addition2x_start)
    arithmetic_mean_addition2x.append(i)
    print(list_addition2x_start)
    list_addition2x_start = []
    print(arithmetic_mean_addition2x)


def subtraction3x():  # ычитание 3-х чисел
    global arithmetic_mean_substraction3x
    right = 0  # number of correct answers
    m = 2
    error = 0
    list_subtraction3x_start = []
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(100, 999)
        second = random.randint(100, 999)
        n = fisrt - second
        print(fisrt, '-', second)
        answer = int(input())
        if right == m:
            break
        if answer == n:
            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            list_subtraction3x_start.append(timenumber)
        else:
            error += 1
            m += 10
            print('Осталось', m - right, ' примеров')
        if right == m:
            break
    s = 0
    for i in list_subtraction3x_start:
        s += i
    i = s / len(list_subtraction3x_start)
    arithmetic_mean_substraction3x.append(i)
    print(list_subtraction3x_start)
    list_subtraction3x_start = []
    print(arithmetic_mean_substraction3x)



def subtraction2x():  # Вычитание 2-х чисел
    right = 0  # number of correct answers
    m = 2      # number of examples
    error = 0  # number of errors
    timelist_subtraction2x = []
    arithmetic_mean_subtraction2x = []
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(10, 99)
        second = random.randint(10, 99)
        n = fisrt - second
        print(fisrt, '-', second)
        answer = int(input())
        if right == m:
            break
        if answer == n:
            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            timelist_subtraction2x.append(timenumber)
        else:
            error += 1
            m += 10
            print('Осталось', m - right, ' примеров')
        if right == m:
            break
    s = 0
    for i in timelist_subtraction2x:
        s += i
    i = s / len(timelist_subtraction2x)
    arithmetic_mean_subtraction2x.append(i)
    print('Значение времени решения каждого примера', timelist_subtraction2x)
    timelist_subtraction2x = []
    print('Среднее значение времени', arithmetic_mean_subtraction2x)

subtraction2x()


def multiplication3x():  # Умножение трехзначных чисел
    right = 0  # number of correct answers
    m = 2      # number of examples
    error = 0  # number of errors
    timelist_multiplication3 = []
    arithmetic_mean_multiplication3x = []
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(100, 999)
        second = random.randint(100, 999)
        n = fisrt * second
        print(fisrt, '*', second)
        answer = int(input())
        if right == m:
            break
        if answer == n:
            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            timelist_multiplication3.append(timenumber)
        else:
            error += 1
            m += 10
            print('Осталось', m - right, ' примеров')
        if right == m:
            break
    s = 0
    for i in timelist_multiplication3:
        s += i
    i = s / len(timelist_multiplication3)
    arithmetic_mean_multiplication3x.append(i)
    print('Значение времени решения каждого примера', timelist_multiplication3)
    timelist_multiplication3 = []
    print('Среднее значение времени', arithmetic_mean_multiplication3x)

multiplication3x()

def multiplication2x():  # Умножение дыухзначных чисел
    right = 0  # number of correct answers
    m = 2      # number of examples
    error = 0  # number of errors
    timelist_multiplication2 = []
    arithmetic_mean_multiplication2x = []
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(10, 99)
        second = random.randint(10, 99)
        n = fisrt * second
        print(fisrt, '*', second)
        answer = int(input())
        if right == m:
            break
        if answer == n:
            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            timelist_multiplication2.append(timenumber)
        else:
            error += 1
            m += 10
            print('Осталось', m - right, ' примеров')
        if right == m:
            break
    s = 0
    for i in timelist_multiplication2:
        s += i
    i = s / len(timelist_multiplication2)
    arithmetic_mean_multiplication2x.append(i)
    print('Значение времени решения каждого примера', timelist_multiplication2)
    timelist_multiplication2 = []
    print('Среднее значение времени', arithmetic_mean_multiplication2x)



def multiplication1x():  # Умножение однозначных чисел
    right = 0  # number of correct answers
    m = 2      # number of examples
    error = 0  # number of errors
    timelist_multiplication1 = []
    arithmetic_mean_multiplication1x = []
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(1, 9)
        second = random.randint(1, 9)
        n = fisrt * second
        print(fisrt, '*', second)
        answer = int(input())
        if answer == n:
            right += 1
            print('Осталось ', m - right, ' примеров')
            tm2 = time.time()
            timenumber = int(tm2 - tm1)
            timelist_multiplication1.append(timenumber)
        else:
            error += 1
            m += 10
            print('Осталось', m - right, ' примеров')
        if right == m:
            break
    s = 0
    for i in timelist_multiplication1:
        s += i
    i = s / len(timelist_multiplication1)
    arithmetic_mean_multiplication1x.append(i)
    print('Значение времени решения каждого примера', timelist_multiplication1)
    timelist_multiplication1 = []
    print('Среднее значение времени', arithmetic_mean_multiplication1x)



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


