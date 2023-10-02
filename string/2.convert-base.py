import string
import functools


def convert_base(num_as_string, base1, base2):
  def construct_from_base(num_as_int, base):
    return '' if num_as_int == 0 else construct_from_base(num_as_int // base, base) + string.hexdigits[
      num_as_int % base].upper()

  is_negative = num_as_string[0] == '-'
  num_as_int = functools.reduce(
    lambda x, c: x * base1 + string.hexdigits.index(c.lower()), num_as_string[is_negative:], 0
  )
  return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, base2))


print("Convert: 1323, b1: 10, b2: 2, result:", convert_base('1323', 10, 2))
print("Convert: 10100101011, b1: 2, b2: 10, result:", convert_base('10100101011', 2, 10))
