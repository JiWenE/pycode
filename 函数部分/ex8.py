# 函数不同调用方法（带返回值和无返回值的）
def cheese_and_cakes(cheese_count, box_of_cake):
    print("你有 %d 个奶酪。" % cheese_count)
    print("你有 %d 个蛋糕" % box_of_cake)
    print('\n')

print("------------------------")
cheese_and_cakes(20, 30)

print("------------------------")
cheese = 10
cake = 30
cheese_and_cakes(cheese, cake)

print("------------------------")
cheese_and_cakes(10+20, 5+6)

print("------------------------")
cheese_and_cakes(cheese + 100, cake + 1000)
