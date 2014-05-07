"""
Prints out subsets of length 1 through length n of an n character long
string.
Example:
>>> subsets("arson")
a
r
s
o
n
ar
rs
so
on
ars
rso
son
arso
rson
arson
"""


def subsets(word):
    i = 0
    while i < len(word):
        j = 0
        while j + i < len(word):
            print word[j:j+i+1]
            j += 1
        i += 1
