# -*- coding: utf-8 -*-
# import math


'''
 k       n!
C  = -----------
 n   k! * (n-k)!
'''

def Binomial_Coefficient(n,k):
    '''
    :param n: n number of combinations // общее число элементов
    :param k: total number of combinations // общее кол-во сочетаний
    :return: the number of combinations of k elements in n // число сочетаний k элементов в n
    '''
    return int((math.factorial(n)) / (math.factorial(k) * (math.factorial(n-k)))) # применяем формулу биноминального коофицента

def Euclid_Method(a,b):
    """
    (10,2) - ok
    (10, 20) - return False, only a > b
    (-5, -2) - return False, only a > 0 and b > 0
    (10,10) - why??

    :param a: any natural number that is greater than b, int or float // любое натуральное число которое больше b, int или float
    :param b: any natural number that is less than a, int or float // любое натуральное число которое меньше a, int или float
    :return: the largest number by which a and b are divided // наибольшее число на которое делится a и b
    """
    if a < b or a <= 0 or b <= 0: return False # условие для корректного ответа
    n = a%b
    while n > 0:
        b%=n
        try: n%=b
        except ZeroDivisionError: return n # обработчик ошибки того что целочисленого нет(например 2%3)
    return b

def Get_Any_Area (lst): # https://youtu.be/vUCJWwGQEYI
    '''
    a two-dimensional array with an arbitrary number of coordinates on a two-dimensional plane is accepted as input,
    the output returns the area of the figure, the number of coordinates is unlimited //
    на вход принимается двухмерный массив с произвольным кол-во координат на двухмерной плоскости,
    на выходе возварщается площадь фигуры, число координат не ограничено\n\n
    the length of the lst is whatever // длина lst какая угодно\n
    for example: [[-4,-2], [2,4], [4,-1]] -> 21.0\n
    for example: [[-4,-2], [-4,1], [-1,4], [2,4], [4,2], [4,-1], [2,-3], [-3,-3]] - > 47.0
    :param lst: [[x1,y1],[x2,y2],[x3,y3]...[x99,y99],[x100,y100], [x101,y101]]
    :return: area in the float type
    '''
    if len(lst) < 2: return 0.0
    i = 1
    x = [0,0]
    x[0] = lst[0][0] * lst[1][1]
    x[1] = lst[0][1] * lst[1][0]
    while i < len(lst)-1:
        i += 1
        n = round(i)
        x[0]+=lst[i-1][0] * lst[i][1]
        x[1]+=lst[i][0] * lst[i-1][1]
    x[0]+= lst[len(lst)-1][0] * lst[0][1]
    x[1] += lst[0][0] * lst[len(lst) - 1][1]
    x = list(sorted(x)) # сортируем значения по возрастанию
    return (x[1] - x[0]) / 2

def Standard_Deviation(lst):
    '''
    eng:
    :param lst: array with arbitrary number of elements
    :return: Float standard deviation
    for example: [5,10,15,20.00000,25] -> 7.0710678118654755
    if the array is empty then the answer is False
    -----------
    rus:
    :param lst: массив с произволным кол-во элементов int или float элементов
    :return: Float среднее квадтратичное отклонение
    for example: [5,10,15,20.00000,25] -> 7.0710678118654755
    если массив пустой то ответ False
    '''
    if len(lst) == 0:
        return False
    answer= 0
    avg = sum(lst) / len(lst)
    for i in lst:
        answer += (i - avg) ** 2
    return (answer / len(lst)) ** 0.5

def Fraction(After_The_Decimal_Point = 0,period = 0):
    '''
    for exapmle: (23,6) mean 0.236666666666... = 213/900; (17,69) mean 0.17696969696969... = 1752/9900
    :param After_The_Decimal_Point: numerator
    :param period: denominator
    :return: fraction
    coming soon:
    - обработчик целых частей
    - сокращение готовой дроби
    - обрботчик ошибок
    - рефакторинг
    '''
    try:
        num1 = int(str(After_The_Decimal_Point)+str(period))
        num2 = int((After_The_Decimal_Point))
    except:
        return False
    len1 = len(str(num1))
    len2 = len(str(num2))
    if num2 == 0: len2 = 0
    mount = 10**len1-10**len2
    return f'{num1-num2}/{mount}'
