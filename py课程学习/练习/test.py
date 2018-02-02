import math
from collections import Iterable

# x = 1
# y = math.sqrt(x)
#
# a = callable(x)
#
# print(x, y, a)
#
#
# def fib(num):
#     result = [0, 1]
#     for i in range(num - 2):
#         result.append(result[-2] + result[-1])
#     return result
#
#
# print(fib(10))
#
#
# def index_of_min(array, offset):
#     index = offset
#     for i in range(offset, len(array)):
#         e = array[i]
#         if array[index] > e:
#             index = i
#         else:
#             continue
#     return index
#
#
#
#
# #　冒泡排序
# def diy_sort(array):
#     l = array
#     for i in range(len(l)):
#         index = index_of_min(l, i)
#         l[i], l[index] = l[index], l[i]
#     return l
#
# i = [2, 4, 5, 2, 4, 5, 7, 8]
# j = [(0,0,0,0), (1,2,34,5), (2,4,6,8)]
# print(diy_sort(i)[:])
# print(sorted(i))
#
#
#
# # 匿名函数lambda
#
# fun = lambda n: n * n
# fun1 = lambda x, y: x/y
# print('lambda', fun(3))
# print('lambda', fun1(6, 3))
#
# # sorted 返回一个值
# # sort 不返回
# print(sorted(j, key=lambda x: x[1]))
#
#
# # 字符串排序
# def reversr_seq(seq):
#     r = list(seq)
#     r.sort(reverse=True)
#     if type(seq) == str:
#         s = ''.join(r)
#         return s
#     else:
#         return type(seq)(r)
#
#
# seq = ('a', 'b', 'c')
# # print(reversr_seq(seq))
#
#
# def ff(a, b=2, *c, **d):  # *c 不定长参数（元组）**d不定长参数(字典)可以不传参
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# ff(1)
# '''
# 输出：
# 1
# 2
# ()
# {}
# '''
# ff(1, 3, 3, 4, 5, x=4, y=5)
# '''
# 输出：
# 1
# 3
# (3, 4, 5)
# {'x': 4, 'y': 5}
# '''
# # 99乘法表
# for i in range(1, 10):
#     j = 1
#     while j <= i:
#         print('%s*%s=%s' % (i, j, i*j), end=' ')
#         j += 1
#     print('')
# a=1
# if a:
#     b=2
# if a:
#     c=b
# print(c)
#
#
# flag = 1
# i = 0
# while(i < 4):
#     if(i > 2):
#         print(i)
#         flag = 0
#         break
#     i+=1
#
# print("flag=", flag)
#
#
# def fun(*args):
#     temp = 1
#     if len(args) == 0:
#         pass
#     else:
#         for i in args:
#             temp = temp * i
#     return temp
#
#
# print('product(5) =', fun(5))
# print('product(5, 6) =', fun(5, 6))
# print('product(5, 6, 7) =', fun(5, 6, 7))
# print('product(5, 6, 7, 9) =', fun(5, 6, 7, 9))
# if fun(5) != 5:
#     print('测试失败!')
# elif fun(5, 6) != 30:
#     print('测试失败!')
# elif fun(5, 6, 7) != 210:
#     print('测试失败!')
# elif fun(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         fun()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')
#
#
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)
#
# move(4, 'A', 'B', 'C')
#
# print(isinstance([1], Iterable))
#
#
# def findMinAndMax(L):
#     if len(L) == 0:
#         return (None, None)
#     else:
#         max = min = L[0]
#         for i in L:
#             if i > max:
#                 max = i
#             elif i < min:
#                 min = i
#     return (min, max)
#
#
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')
#
#
# # -*- coding: utf-8 -*-
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')
#
#
# # 生成器generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# def fib2(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# fib(6)
#
# for n in fib2(6):
#     print(n)


# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]
# def triangle(n):
#     L = [1]
#     while True:
#         yield L
#         L = [L[x]+L[x+1] for x in range(len(L)-1)]
#         L.insert(0, 1)
#         L.append(1)
#         if len(L) > 10:
#             break
#
# results = []
# k = 0
# a = triangle(10)
# for t in a:
#     print(t)
#     results.append(t)
#     k = k + 1
#     if k == 10:
#         break
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# def normalize(name):
#     return name[:1].upper()+name[1:len(name)].lower()
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# from functools import reduce
#
#
# def multiply(x, y):
#     return x*y
#
#
# def prod(L):
#     return reduce(multiply, L)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def char2num(s):
#     return DIGITS[s]
#
#
# def str2float(s):
#     L = s.split('.')
#     return reduce(lambda x, y: x*10+y, map(char2num, L[0]))+reduce(lambda x, y: x*0.1+y, map(char2num, L[1][::-1]))/10
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def is_palindrome(n):
#     return int(str(n)[::-1]) == n
#
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]

print(sorted(L, key=by_score))
print(sorted(L, key=by_name))
