""" Utilities """
import string
import random


def randomString(stringLength):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(symbols) for i in range(stringLength))


def toStr(arr):
    resul = ""
    for item in arr:
        resul += item
    return resul


def toComma(arr):
    resul = ""
    for item in arr:
        resul += str(item) + ","

    return resul[:-1]


def max_bits(x): return x ** 2
