""" Utilities """
import string
import random

def max_bits(x):

    return 

def randomString(stringLength):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(symbols) for i in range(stringLength))