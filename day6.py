import numpy as np
# import matplotlib.pyplot as plt
import scipy as sp
from sklearn import datasets
import sys
import random
import math

MaxNum = sys.maxsize

# print('hello', 'world', sep=',')
# a = 8
# b = 12.2342
# c = 1 + 2j
# d = 'hello world'
# e = True
#
# print(type(a), type(b), type(c), type(d), type(e), sep=', ', end='\n')
# print('%d, %f, %.1f + %.1fj, %s, %r' % (a, b, c.real, c.imag, d, e), end='\n')
# print('{}, {}, {} + {}j, {}, {}'.format(a, b, c.real, c.imag, d, e), end='\n')
#
# # convert temperature from F to C Gage
# f_temp = float(input('temperature in F: \n'))
# c_temp = (f_temp - 32) / 1.8
# print('%.2f F tempertuare equals to %.2f C temperature' % (f_temp, c_temp))
#
# # determine if the input is a leap year
# year = int(input('input a year: \n'))
# is_leap = (year % 4 == 0 and year % 100 != 0) or \
#             year % 400 == 0
# print('%d year is a leap year? %r' % (year, is_leap))
#
# UN = input('username: ')
# PW = input('password: ')
#
# if UN == 'admin' and PW == '0527':
#     print('welcome')
# elif UN == 'admin' and PW != '0527':
#     print('wrong pw')
# elif UN != 'admin' and PW == '0527':
#     print('wrong un')
# else:
#     print('incorrect')

# ############# for statement
# SUM = 0
#
# for i in range(2, 101, 2):
#     SUM += i
# print('summed number is %d, current i is %d' % (SUM, i))
#
# answer = random.randint(1, 100)
# counter = 0

# ############  while statement
# while True:
#     counter += 1
#     number = int(input('put in an interger: \n'))
#     if number < answer:
#         print('try a larger number.')
#     elif number > answer:
#         print('try a smaller number')
#     else:
#         print('correct, the answer is %d' %answer)
#         break
# print('you tried %d times' %counter)
# if counter > 7:
#     print('pls check your iq xD')

# ########### number table
# for i in range(1, 10, 1):
#     for j in range(1, 10, 1):
#         print('%d\t' % (i*j), end='')
#     print('\n')



# ################ prime number check

# num = int(input('input an integer:\n'))
# end = int(math.sqrt(num))
#
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and x != 1:
#     print('%d is a prime number' % (num))
# else:
#     print('%d is not a prime number' % (num))

# ################
# for num in range(100, 1000, 1):
# #     if (num // 100)**3 + (num % 100 // 10)**3 + (num % 10)**3 == num:
# #         print('%5d is the number we need\n' % num)

# #################
# def FAC(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result
#
# X = int(input('larger integer X: '))
# Y = int(input('smaller integer Y: '))
#
# print(FAC(X))
# print(FAC(X) // FAC(Y) // FAC(X - Y))

# #####################

def roll_dice(n = 2):
    '''
    roll dice and add up
    :param n: # of times
    :return: added number
    '''
#     total = 0
#     for _ in range(n):
#         total += random.randint(1, 6)
#     return total
#
#
# print(roll_dice(4))

# ###################################
def add_(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add_(3, 4, 10))

####################################
# from module1 import foo
# foo()
# from module2 import foo
# foo()

####################################
# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if y % factor == 0 and x % factor == 0:
#             return factor
#
# def lcm(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(y, x*y +1):
#         if factor % x == 0 and factor % y == 0:
#             return factor
#
# print(gcd(5, 7))
# print(lcm(12, 7))

########################################
# def is_prime(num):
#     for factor in range(2, num):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False
#
# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp = temp // 10
#     return num == total
#
#
# if __name__ == '__main__':
#     num = int(input('input an integer:\n'))
#     if is_palindrome(num) and is_prime(num):
#         print('%d is palindrome and prime' %num)
#     else:
#         print('%d is not palindrome and prime' %num)

#################################################
def foo():
    global a    # try to avoid global variable
    a = 200
    print(a)

if __name__ == '__main__':
    a = 100
    foo()
    print(a)

############################################
def main():
    print('main function')
    pass

if __name__ == '__main__':
    main()
    print('back to main')
