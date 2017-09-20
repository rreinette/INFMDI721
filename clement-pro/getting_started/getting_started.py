from math import floor, cos, pi
# import scipy as sp
# import numpy as np
# import matplotlib as plt
# import pandas as pd
import sklearn.linear_model as lm
from my_module import *
from IPython.core.debugger import set_trace
import os


def digit_sum(n):
    result = 0
    exp = 0
    #  set_trace()  # set a breakpoint # usefuls cmds: s(tep) n(ext) unt(il) r(eturn) c(continue)

    while int(floor(float(n) / 10 ** exp)) > 0:
        result += int(floor(float(n) / 10 ** exp) - floor(float(n) / 10 ** (exp + 1)) * 10)
        exp += 1

    return result


print(digit_sum(1002))

print(censor("hey hey hey", "hey"))


#  print(os.getcwd())
dirname = "../file1/"
if not os.path.exists(dirname):
    os.mkdir(dirname)
file1 = open(dirname + "file1.txt", "w")
file1.write("le chat le chien\nla petite la grosse\n\ncoucou toi comment va toi")
file1.close()


my_dict = {'a': 1, 'b': 2, 'd': 4}
print(my_dict.__len__())
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(my_dict['a'])
if 'c' in my_dict:
    print(my_dict['c'])
my_dict.pop('b')  # returns value
my_dict.popitem()  # whichever - returns tuple
print(my_dict)
del my_dict['a']
print(my_dict)
my_dict.clear()


my_list = list(range(1, 11))
my_list.__len__()
my_list.append(0)
my_list.count(1)
my_list.reverse()
my_list.insert(5, 1)
my_list.pop(5)  # index
my_list.remove(5)  # value
del my_list[9]
my_list.sort(key=None, reverse=True)
print(my_list)


def count_words(text):
    list_words = text.split(" ")
    result = {}
    for word in list_words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result


should_return = True  # Variable globale


def most_frequent_word_in_each_paragraph(filename):
    result = []

    with open(filename) as file:
        for paragraph in file:
            if paragraph != "\n":
                dict_count = count_words(paragraph.rstrip("\n"))
                result.append(most_frequent_word(dict_count))

    if should_return:
        return result
    else:
        return []


def most_frequent_word(dict_count):
    most_frequent = ""
    max_count = 0
    for word in dict_count:
        if dict_count[word] > max_count:
            most_frequent = word
            max_count = dict_count[word]
    return most_frequent


my_dict_count = count_words("le chien le chien petit gros petit le")
print(my_dict_count)
print(most_frequent_word(my_dict_count))
print(most_frequent_word_in_each_paragraph("../file1/file1.txt"))

with open("../file1/file1.txt") as f:
    print([line.rstrip('\n') for line in f])
    print(f.readlines())
    print(list(f))
print(f.closed)

my_int = 2
print("The value of my_int is", my_int, ".")  # add spaces
print("The value of my_int is " + str(my_int) + " and not " + str(cos(pi)) + ".")
print("I need %s minutes please." % my_int)


def switch(my_string):
    return {'hi': 0, 'hello': 1, 'coucou': 2}[my_string]


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')  # appends
        a, b = b, a + b
    print()  # new line


t = ('elephant', 1, {'hi': 0, 'hello': 1})
print(type(t))


def f(ham: str, eggs: str = 'eggs') -> str:
    return ham + eggs


print(f.__annotations__)
print(f("spam"))
print(f("spam", "pasta"))
