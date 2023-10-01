import functools
import string


arr = [1, 3, 2, 1, 43, 23, 22]
s = "1321432322"
print("summation of list: ", functools.reduce(lambda a, b: a + b, arr))
print("summation of string: ", functools.reduce(lambda a, b: a + string.digits.index(b), s, 0))
print("max: ", functools.reduce(lambda a, b: a if a > b else b, arr))

