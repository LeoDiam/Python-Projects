import string

import sre_yield
s = 'L(OL)+'
print(list(sre_yield.AllStrings(s, max_count=5, charset=string.ascii_uppercase)))
j = 'crossword[j].word_number', " ",' regex[i]', " ", 'regex_list[k]'
print(j[0])
# Python3 code to demonstrate
# test for values in tuple of tuple
# using any()

# initializing tuple of tuple
test_tuple = (("geeksforgeeks", "gfg"), ("CS_Portal", "best"))

# printing tuple
print ("The original tuple is " + str(test_tuple))

# using any()
# to test for value in tuple of tuple
if (any('geeksforgeeks' in i for i in test_tuple)) :
	print("geeksforgeeks is present")
else :
	print("geeksforgeeks is not present")
