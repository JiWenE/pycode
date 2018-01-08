import math

x = 1
y = math.sqrt(x)

a = callable(x)

print(x, y, a)


def fib(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


print(fib(10))


def index_of_min(array, offset):
    index = offset
    for i in range(offset, len(array)):
        e = array[i]
        if array[index] > e:
            index = i
        else:
            continue
    return index




#　冒泡排序
def diy_sort(array):
    l = array
    for i in range(len(l)):
        index = index_of_min(l, i)
        l[i], l[index] = l[index], l[i]
    return l

i = [2, 4, 5, 2, 4, 5, 7, 8]
j = [(0,0,0,0), (1,2,34,5), (2,4,6,8)]
print(diy_sort(i)[:])
print(sorted(i))



# 匿名函数lambda

fun = lambda n: n * n
fun1 = lambda x, y: x/y
print('lambda', fun(3))
print('lambda', fun1(6, 3))

# sorted 返回一个值
# sort 不返回
print(sorted(j, key=lambda x: x[1]))


# 字符串排序
def reversr_seq(seq):
    r = list(seq)
    r.sort(reverse=True)
    if type(seq) == str:
        s = ''.join(r)
        return s
    else:
        return type(seq)(r)


seq = ('a', 'b', 'c')
# print(reversr_seq(seq))


def ff(a, b=2, *c, **d):  # *c 不定长参数（元组）**d不定长参数(字典)可以不传参
    print(a)
    print(b)
    print(c)
    print(d)
ff(1)
'''
输出：
1
2
()
{}
'''
ff(1, 3, 3, 4, 5, x=4, y=5)
'''
输出：
1
3
(3, 4, 5)
{'x': 4, 'y': 5}
'''
# 99乘法表
for i in range(1, 10):
    j = 1
    while j <= i:
        print('%s*%s=%s' % (i, j, i*j), end=' ')
        j += 1
    print('')
a=1
if a:
    b=2
if a:
    c=b
print(c)