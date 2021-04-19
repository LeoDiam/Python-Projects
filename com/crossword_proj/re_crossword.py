import re
import csv
import string
import sys
import sre_yield
from cross import Cross


def read_csv(csv_crossword_filename):
    lst = []
    with open(csv_crossword_filename) as csv_file:
        for line in csv_file:
            arr = line.split(',')
            word_number = arr[0]
            num_dots = arr[1]
            dic = {}
            for i in range(2, len(arr), 2):
                if '\n' in arr[i + 1]:
                    dic[arr[i]] = arr[i + 1][:-1]
                else:
                    dic[arr[i]] = arr[i + 1]
            cr = Cross(word_number, num_dots, dic)
            lst.append(cr)
    return lst


def read_txt(txt_regular_expressions_filename):
    lst = []
    with open(txt_regular_expressions_filename) as txt_file:
        for line in txt_file:
            lst.append(line[:-1])
    return lst


csv_crossword_filename = sys.argv[1]
txt_regular_expressions_filename = sys.argv[2]
crosswords = read_csv(csv_crossword_filename)

# print(crosswords)
#
# regexs = read_txt(txt_regular_expressions_filename)
#
# print(regexs)
# crosswords[3].replace_dot(crosswords[11])
#
# # crosswords[3].try_regex('')
# a = list(sre_yield.AllStrings(regexs[0], max_count=5, charset=string.ascii_uppercase))
# print(a)
#
# x len(crossword[i])
#
# if h opoia 8a diatrexei ola ta stoixeia tis listas crosswords
# opoio exei num_of_dots pou na periexei stoixeia ektos apo teleies
# LOLOLOL
# ..W....