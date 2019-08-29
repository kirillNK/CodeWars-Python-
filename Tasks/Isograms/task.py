"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

Link: https://www.codewars.com/kata/isograms/train/python
"""


# def is_isogram(string):
#     if len(string) == 0:
#         return True
#     else:
#       for item in string.lower():
#         if string.count(item) > 1:
#           return False
#         else:
#           return True


def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)


is_isogram("Dermatoglyphics")
is_isogram("aba")
is_isogram("moOse")
