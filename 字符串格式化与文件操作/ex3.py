# 问卷调查系列QAQ
from sys import argv

script, user_name = argv

prompt = '>'


print("hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you some questions.")
print("Do you like me %s" % user_name)
likes = input(prompt)

print("Where do you live %s" % user_name)
lives = input(prompt)

print("what is your phone number?")
num = input(prompt)

print("""Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And your phone number is %r.""" % (likes, lives, num))

