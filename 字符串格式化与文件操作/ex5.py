# 文件操作 写入
from sys import argv
script, filename = argv

print("we are going to earse %r." % filename)
print("if you don't want that, hit CTRL-C (^C).")
print("if you want that, hit RETURN")
input("?")

print("Opening the file..........")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")

target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("i'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("file closing.....")
target.close()  # 这步很重要
