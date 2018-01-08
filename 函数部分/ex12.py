# 条件语句
people = 30
cars = 40
buses = 15

if cars > people:
    print("haha！")
else:
    print("hehe!")


# 循环和列表
hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weight = [1, 2, 3, 4]


for hair in hairs:
    print("this hair is %s." % hair)

# append() 用法
elements = []

for i in weight:
    elements.append(i)
print(elements)

# range() 方法使用
list1 = []
for j in range(1, 10):
    list1.append(j)
print(list1)
# 分片
print(list1[2:4])
print(list1[-7:-5])


# while 循环
i = 0
number = []

while i<6:
    number.append(i)
    i += 1
print(number)


class T(object):
    def test(self):
        print(self)
a = T()
a.test()
