# 文件操作 拷贝
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))
input1 = open(from_file)
indata1 = input1.read()

print("the input file is %d bytes long" % len(indata1))
print("does the file exist? %r" % exists(to_file))
print("ready hit RETURN to continue, CTRL_C to stop")
input()

output = open(to_file, 'w')
output.write(indata1)

print("done")

output.close()
input1.close()
# 以上代码可简化为一行 open(to_file, 'w').write(len(open(from_file).read()))
