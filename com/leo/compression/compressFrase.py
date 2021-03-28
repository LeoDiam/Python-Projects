text = "This is the phrase that we want to compress."
#
# symb2freq = {}
# for ch in text:
#     # If ch is not in the frequency table
#     # we have to create an entry for it
#     # initialized to zero.
#     if ch not in symb2freq:
#         symb2freq[ch] = 0
#     # Add one to the number of times we have
#     # seen ch.
#     symb2freq[ch] += 1
#
#
#
# pprint.pprint(symb2freq)


# second way
# from collections import defaultdict
#
# symb2freq = defaultdict(int)
# for ch in text:
#        symb2freq[ch] += 1
# import pprint
# pprint.pprint(symb2freq)
from collections import Counter

symb2freq = Counter(text)
import pprint
pprint.pprint(symb2freq)