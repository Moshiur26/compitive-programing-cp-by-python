import functools
import string


def int_to_string(x):
  is_negative = False
  if x < 0:
    is_negative = True

  s = []
  while True:
    s.append(chr(ord('0') + x % 10))
    x //= 10
    if x == 0:
      break

  return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
  return functools.reduce(
    lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


print(int_to_string(10) + int_to_string(43))
print(string_to_int('10') + string_to_int('43'))
