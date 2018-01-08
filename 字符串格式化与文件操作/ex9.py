# 函数与文操作的结合QAQ
from sys import argv
script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("the whole file is:\n")
print_all(current_file)

print("each line is:\n")
rewind(current_file)

current_line = 1
while current_line <= 3:
    print_a_line(current_line, current_file)
    current_line = current_line + 1

