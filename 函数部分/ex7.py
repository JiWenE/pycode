def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))


def print_two_again(arg3, arg4):
    print("arg1: %r, arg2: %r" % (arg3, arg4))
# 注意以上两个函数定义方式


def print_one(arg5):
    print("arg1: %r" % arg5)


print_two("abc", "def")
print_two_again("abc", "def")
print_one("first")
