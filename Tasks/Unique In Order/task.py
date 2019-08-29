"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

Link: https://www.codewars.com/kata/unique-in-order/train/python
"""

str1 = "AAAABBBCCDAABBB"
str2 = "ABBCcAD"
str3 = [1, 2, 2, 3, 3]
str4 = "A"
str5 = "AA"


# def unique_in_order(iterable):
#     answerList = []
#     if len(iterable) == 1:
#         return [iterable]
#     elif len(iterable) == 2:
#         if iterable[0] == iterable[1]:
#             return [iterable[0]]
#     else:
#         for item in range(len(iterable)):
#             if iterable[item - 1] == iterable[item]:
#                 pass
#             else:
#                 answerList.append(iterable[item])
#
#         return answerList

def unique_in_order(iterable):
    answerList = []
    prevItem = None
    for item in iterable:
        if item != prevItem:
            answerList.append(item)
            prevItem = item
    return answerList


unique_in_order(str1)
unique_in_order(str2)
unique_in_order(str3)
unique_in_order(str4)
unique_in_order(str5)
