x = "There are %d tyoes of people." % (10)
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x, '\n', y)
print(x)
print(y)
print("i said:%r"% x)
print("i also said:'%s'" % y)

hilarious = False
joke_evluation = "Isn't that a joke so funny?! %r"
print(joke_evluation % hilarious)

print("." * 10)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
print(end1 + end2 + end3 + end4 + end5 + end6)

print("how old are you")
age = input()
print("how tall are you")
height = input()
print("so, you are %s old, %s tall"%(age, height))
