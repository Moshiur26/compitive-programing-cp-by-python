import functools


def spreadsheet_col_decode(col):
  return functools.reduce(
    lambda value, c: value * 26 + ord(c) - ord('A') + 1, col, 0
  )


print("AZ: ", spreadsheet_col_decode('AZ'))
print("ZZ: ", spreadsheet_col_decode('ZZ'))
print("P: ", spreadsheet_col_decode('P'))
print("ABZZK: ", spreadsheet_col_decode('ABZZK'))
