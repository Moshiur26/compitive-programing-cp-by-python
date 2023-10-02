def remove_2_replace_7_by_8_and_9(size, arr):
  number_of_7, write_index = 0, 0
  for i in range(size):
    if arr[i] != 2:
      arr[write_index] = arr[i]
      write_index += 1
    if arr[i] == 7:
      number_of_7 += 1

  current_index = write_index - 1
  replace_index = write_index + number_of_7 - 1
  final_size = write_index + number_of_7

  while current_index >= 0:
    if arr[current_index] == 7:
      arr[replace_index] = 9
      arr[replace_index - 1] = 8
      replace_index -= 2
    # if not match with 7
    else:
      arr[replace_index] = arr[current_index]
      replace_index -= 1
    current_index -= 1
  return arr[:final_size]


print("[1, 2, 4, 7, 8, 2, 0, 7, 1] ->: ", remove_2_replace_7_by_8_and_9(9, [1, 2, 4, 7, 8, 2, 0, 7, 1]))
print("[1, 2, 4, 2, 2, 7, 2, 2, 8, 2, 0, 7, 1] ->: ", remove_2_replace_7_by_8_and_9(13, [1, 2, 4, 2, 2, 7, 2, 2, 8, 2, 0, 7, 1]))
