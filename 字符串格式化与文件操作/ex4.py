# 文件操作'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open a disk file for updating (reading and writing)
# 'U' universal newlines mode (deprecated)

from sys import argv
script, filename = argv

txt = open(filename, 'r', encoding='utf-8')

print("Here's your file %r:" % filename)
print(txt.read())
txt.close()
print("Type the filename again:")
file_again = input(">>>")

txt_again = open(file_again, 'r', encoding='utf-8')

print(txt_again.read())
txt_again.close()
