
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')  # 以空格为分隔符将其转换为列表
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)  # 排序


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)  # 移除当前位置的元素
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

sentence = "All good things come to those who wait."
print(break_words(sentence))
print(sort_words(break_words(sentence)))
print_first_word(break_words(sentence))
print_last_word(break_words(sentence))
