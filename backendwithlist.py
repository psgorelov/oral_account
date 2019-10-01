import random
from itertools import product
import time
from typing import List

def arithmetic_mean(lst): #среднее арифметическое 
    s = 0
    for i in lst:
        s += i
    print(s / len(lst))
P
    
def addition3x():  # сложение трехзначных чисел
    right = 0 #number of correct answers
    m = 2
    error = 0
    global timelist
    timelist = []
    global arithmetic_mean_list
    arithmetic_mean_list = []
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(100, 999)
        second = random.randint(100, 999)
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
            timelist.append(timenumber) 
        else:
            error += 1
            m += 10
            print('Осталось', m, ' примеров')
        if right == m:
            break
    print(timelist)    
    arithmetic_mean(timelist)

addition3x()
arithmetic_mean_list.append(arithmetic_mean(timelist))
print(arithmetic_mean_list)



def addition2x():  # Cложение 2-х значных чисел ГОТОВО
    right = 0 #number of correct answers
    m = 2
    error = 0
    timelist_addition2 = []
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
            timelist_addition2.append(timenumber) 
        else:
            error += 1
            m += 10
            print('Осталось', m, ' примеров')
        if right == m:
            break
    print(timelist_addition2)    
    arithmetic_mean(timelist_addition2)



def subtraction3x():  # ычитание 3-х чисел
    right = 0 #number of correct answers
    m = 2
    error = 0
    timelist_subtraction3 = []
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
            timelist_subtraction3.append(timenumber) 
        else:
            error += 1
            m += 10
            print('Осталось', m, ' примеров')
        if right == m:
            break
    print(timelist_subtraction3)    
    arithmetic_mean(timelist_subtraction3)


def subtraction2x():  # Вычитание 2-х чисел
    right = 0 #number of correct answers
    m = 2
    error = 0
    timelist_subtraction2 = []
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
            timelist_subtraction2.append(timenumber) 
        else:
            error += 1
            m += 10
            print('Осталось', m, ' примеров')
        if right == m:
            break
    print(timelist_subtraction2)    
    arithmetic_mean(timelist_subtraction2)

def multiplication3x():  # Умножение трехзначных чисел
    right = 0 #number of correct answers
    m = 2
    error = 0
    timelist_multiolication3 = []
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
            print('Осталось', m, ' примеров')
        if right == m:
            break
    print(timelist_multiplication3)    
    arithmetic_mean(timelist_multiplication3)

def multiplication2x():  # Умножение дыухзначных чисел
    right = 0 #number of correct answers
    m = 2
    error = 0
    timelist_multiolication2 = []
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
            print('Осталось', m, ' примеров')
        if right == m:
            break
    print(timelist_muultiplication2)    
    arithmetic_mean(timelist_multiplication2)
    

def multiplication1x():  # Умножение однозначных чисел
    right = 0 #number of correct answers
    m = 2
    error = 0
    timelist_multiolication1 = []
    while right <= m:
        tm1 = time.time()
        fisrt = random.randint(1, 9)
        second = random.randint(1, 9)
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
            timelist_multiplication1.append(timenumber) 
        else:
            error += 1
            m += 10
            print('Осталось', m, ' примеров')
        if right == m:
            break
    print(timelist_multiplication1)    
    arithmetic_mean(timelist_multiplication1)


def division3x():  # Деление
    time1 = time.time()
    a = 0
    examples = 2
    pairs = [(den, res) for (den, res) in product(range(2, 51), repeat = 2) if
             den * res <= 1000]  # подбор рандомных чисел
    for i, (den, res) in enumerate(random.sample(pairs, 15)):
        print("{}) Сколько будет {} / {} = ?".format(i + 1, den * res, den))
        res2 = int(input("Ответ: "))
        if res2 == res:
            examples -= 1
            print('Вы правы! Осаталось примеров: ', examples)
        else:
            examples += 10
            print('Вы неправы, ответ:', res, "Осталось примеров: ", examples)
        if examples == 0:
            print('Поздравляю, но это только начало) ну или конец, только конец, это начало чего-то хорошего или '
                  'плохого')
            print('Ваше время решения деления: ', int(time.time() - time1) // 60, ' минут', int(time.time() - time1) % 60, ' секунд')
            minute = int(time.time() - time1) // 60
            seconds = int(time.time() - time1) % 60
            
            print(table)
            break


def division2x():  # Деление
    time1 = time.time()
    a = 0
    examples = 2
    pairs = [(den, res) for (den, res) in product(range(2, 51), repeat = 2) if
             den * res <= 100]  # подбор рандомных чисел
    for i, (den, res) in enumerate(random.sample(pairs, 15)):
        print("{}) Сколько будет {} / {} = ?".format(i + 1, den * res, den))
        res2 = int(input("Ответ: "))
        if res2 == res:
            examples -= 1
            print('Вы правы! Осаталось примеров: ', examples)
        else:
            examples += 10
            print('Вы неправы, ответ:', res, "Осталось примеров: ", examples)
        if examples == 0:
            print('Поздравляю, но это только начало) ну или конец, только конец, это начало чего-то хорошего или '
                  'плохого')
            print('Ваше время решения деления: ', int(time.time() - time1) // 60, ' минут', int(time.time() - time1) % 60, ' секунд')
            minute = int(time.time() - time1) // 60
            seconds = int(time.time() - time1) % 60
            table: List[int] = [ minute, seconds]
            print(table)
            break


print(timelist_multiplication2)
