"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret
question is still correct. However, since someone could look over your shoulder, you don't want that shown
on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"

Link: https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
"""

str1 = "4556364607935616"
str2 = "64607935616"
str3 = "123"
str4 = ""


def maskify(cc):
    strLen = len(cc)
    if strLen <= 4:
        return cc
    else:
        result = ("#" * (strLen - 4))
        result += cc[strLen - 4:]
    return result


print(maskify(str1))
print(maskify(str2))
print(maskify(str3))
print(maskify(str4))

