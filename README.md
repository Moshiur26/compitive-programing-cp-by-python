 **String**
----

### String generals:
 ```
import functools
import string

arr = [1, 3, 2, 1, 43, 23, 22]
s = "1321432322"
print("summation of list: ", functools.reduce(lambda a, b: a + b, arr))
print("summation of string: ", functools.reduce(lambda a, b: a + string.digits.index(b), s, 0))
print("max: ", functools.reduce(lambda a, b: a if a > b else b, arr))
```

### Convert String And Integer:
 ```
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
```


### Convert Base:
 ```
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
```


### Spreadsheet Column Decoding:
 ```
import functools


def spreadsheet_col_decode(col):
  return functools.reduce(
    lambda value, c: value * 26 + ord(c) - ord('A') + 1, col, 0
  )


print("AZ: ", spreadsheet_col_decode('AZ'))
print("ZZ: ", spreadsheet_col_decode('ZZ'))
print("P: ", spreadsheet_col_decode('P'))
print("ABZZK: ", spreadsheet_col_decode('ABZZK'))
```


### Remove 2 And Replace 7 By 8 And 9 From Array:
solving this problem within O(n) time complexity
 ```
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
```




**Binary Tree**
----

### Binary Tree Structure:
 ```
class BinaryTreeNode:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
```

**Tree Traversal**
* **Inorder Traverse**
```
def inorder_traversal(tree):
  if tree:
    inorder_traversal(tree.left)
    print(tree.data, end=' ')
    inorder_traversal(tree.right)
```

* **Preorder Traverse**
```
def preorder_traversal(tree):
  if tree:
    print(tree.data, end=' ')
    preorder_traversal(tree.left)
    preorder_traversal(tree.right)
```

* **Postorder Traverse**
```
def postorder_traversal(tree):
  if tree:
    postorder_traversal(tree.left)
    postorder_traversal(tree.right)
    print(tree.data, end=' ')
```

* **Test If Binary Tree Is Height Balanced**
```
import collections


def is_balanced_binary_tree(tree):
  BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithTuple', ('balanced', 'height'))

  def check_balanced(tree):
    if not tree:
      return BalancedStatusWithHeight(True, -1)

    left_result = check_balanced(tree.left)
    if not left_result.balanced:
      return BalancedStatusWithHeight(False, 0)

    right_result = check_balanced(tree.right)
    if not right_result.balanced:
      return BalancedStatusWithHeight(False, 0)

    is_balanced = abs(left_result.height - right_result.height) <= 1
    height = max(left_result.height, right_result.height) + 1
    return BalancedStatusWithHeight(is_balanced, height)

  return check_balanced(tree).balanced
```

* **Test The Solution**
```
from binaryTreeNode import BinaryTreeNode


root = BinaryTreeNode(8)
root.left = BinaryTreeNode(4)
root.right = BinaryTreeNode(5)

root.left.left = BinaryTreeNode(344)
root.left.right = BinaryTreeNode(42)
root.right.left = BinaryTreeNode(32)
root.right.right = BinaryTreeNode(53)

root.left.left.left = BinaryTreeNode(344)
root.left.left.right = BinaryTreeNode(344)
# root.left.right.left = BinaryTreeNode(42)
# root.left.right.right = BinaryTreeNode(24)
root.right.left.left = BinaryTreeNode(32)
root.right.left.right = BinaryTreeNode(43)
root.right.right.left = BinaryTreeNode(53)
root.right.right.right = BinaryTreeNode(23)

print('Tree Balanced Status: %d' % is_balanced_binary_tree(root))
```

* ### LCA(Lowest Common Ancestor):
Time complexity is O(n) And Space complexity is O(h). Here n is number of node and h is tree height.
```
import collections
from binaryTreeNode import BinaryTreeNode


def lca(tree, node0, node1):
  Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

  def lca_helper(tree, node0, node1):
    if not tree:
      return Status(0, None)

    left_result = lca_helper(tree.left, node0, node1)
    if left_result.num_target_nodes == 2:
      return left_result

    right_result = lca_helper(tree.right, node0, node1)
    if right_result.num_target_nodes == 2:
      return right_result

    num_target_nodes = left_result.num_target_nodes + right_result.num_target_nodes + int(tree is node0) + int(tree is node1)
    return Status(num_target_nodes, tree if num_target_nodes == 2 else None)
  return lca_helper(tree, node0, node1)


root = BinaryTreeNode(8)
root.left = BinaryTreeNode(4)
root.right = BinaryTreeNode(5)

root.left.left = BinaryTreeNode(344)
root.left.right = BinaryTreeNode(42)
root.right.left = BinaryTreeNode(32)
root.right.right = BinaryTreeNode(53)

root.left.left.left = BinaryTreeNode(344)
root.left.left.right = BinaryTreeNode(344)
# root.left.right.left = BinaryTreeNode(42)
# root.left.right.right = BinaryTreeNode(24)
root.right.left.left = BinaryTreeNode(32)
root.right.left.right = BinaryTreeNode(43)
root.right.right.left = BinaryTreeNode(53)
root.right.right.right = BinaryTreeNode(23)

result = lca(root, root.right.right.right, root.right.left.left)
result = result.ancestor.data if result.ancestor else 'There is no ancestor'
print('Tree Balanced Status: %d' % result)
```


* ### LCA(Lowest Common Ancestor) Reduce Space Complexity:
This Solution is only applicable when node have parent pointer. Time complexity is O(n) And Space complexity is O(1). Here n is number of node in the tree.
```
def lca(node0, node1):
  def get_depth(node):
    depth = 0
    while node:
      depth += 1
      node = node.parent
    return depth

  depth0, depth1 = get_depth(node0), get_depth(node1)

  if depth1 > depth0:
    node0, node1 = node1, node0

  depth_diff = abs(depth0 - depth1)

  while depth_diff:
    node0 = node0.parent
    depth_diff -= 1

  while node0 is not node1:
    node0 = node0.parent
    node1 = node1.parent
  return node0


class BinaryTreeNode:
  def __init__(self, data=None, parent=None, left=None, right=None):
    self.data = data
    self.parent = parent
    self.left = left
    self.right = right


root = BinaryTreeNode(8)
root.left = BinaryTreeNode(4, root)
root.right = BinaryTreeNode(5, root)

root.left.left = BinaryTreeNode(344, root.left)
root.left.right = BinaryTreeNode(42, root.left)
root.right.left = BinaryTreeNode(32, root.right)
root.right.right = BinaryTreeNode(53, root.right)

root.left.left.left = BinaryTreeNode(344, root.left.left)
root.left.left.right = BinaryTreeNode(344, root.left, root.left.left)
# root.left.right.left = BinaryTreeNode(42, root.left.right)
# root.left.right.right = BinaryTreeNode(24, root.left.right)
root.right.left.left = BinaryTreeNode(32, root.right.left)
root.right.left.right = BinaryTreeNode(43, root.right.left)
root.right.right.left = BinaryTreeNode(53, root.right.right)
root.right.right.right = BinaryTreeNode(23, root.right.right)

result = lca(root.right.right.right, root.right.left.left)
print('Tree Balanced Status: %d' % result.data)
```


* ### Sum Root To Leaf:
Time complexity is O(n) And Space complexity is O(h).
```
from binaryTreeNode import BinaryTreeNode


def sum_root_to_leaf(tree, partial_sum=0):
  if not tree:
    return 0

  partial_sum = partial_sum * 2 + tree.data

  if not tree.left and not tree.right:
    return partial_sum

  return sum_root_to_leaf(tree.left, partial_sum) + sum_root_to_leaf(tree.right, partial_sum)


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(0)
root.right = BinaryTreeNode(1)

root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(1)
root.right.left = BinaryTreeNode(0)
root.right.right = BinaryTreeNode(1)

root.left.left.left = BinaryTreeNode(1)
root.left.left.right = BinaryTreeNode(0)
root.left.right.left = BinaryTreeNode(0)
root.left.right.right = BinaryTreeNode(1)
root.right.left.left = BinaryTreeNode(0)
root.right.left.right = BinaryTreeNode(1)
root.right.right.left = BinaryTreeNode(1)
root.right.right.right = BinaryTreeNode(0)

print('Summation: %d' % sum_root_to_leaf(root))
```


* ### Has Path Sum:
Time complexity is O(n) And Space complexity is O(h).
```
from binaryTreeNode import BinaryTreeNode


def has_path_sum(tree, remaining_sum):
  if not tree:
    return False

  if not tree.left and not tree.right:
    return tree.data == remaining_sum
  return has_path_sum(tree.left, remaining_sum - tree.data) or has_path_sum(tree.right, remaining_sum - tree.data)


root = BinaryTreeNode(8)
root.left = BinaryTreeNode(4)
root.right = BinaryTreeNode(5)

root.left.left = BinaryTreeNode(344)
root.left.right = BinaryTreeNode(42)
root.right.left = BinaryTreeNode(32)
root.right.right = BinaryTreeNode(53)

print("8+5+53: %s" % str(has_path_sum(root, 8+5+53)))
print("8+5+2: %s" % str(has_path_sum(root, 8+5+2)))
```



* ### Inorder Traversal Avoiding Recursion:
Time complexity is O(n) And Space complexity is O(h).
```
from binaryTreeNode import BinaryTreeNode


def inorder_traverse(tree):
  s, result = [], []

  while s or tree:
    if tree:
      s.append(tree)
      tree = tree.left
    else:
      tree = s.pop()
      result.append(tree.data)
      tree = tree.right
  return result


root = BinaryTreeNode(8)
root.left = BinaryTreeNode(4)
root.right = BinaryTreeNode(5)

root.left.left = BinaryTreeNode(344)
root.left.right = BinaryTreeNode(42)
root.right.left = BinaryTreeNode(32)
root.right.right = BinaryTreeNode(53)

print("Inorder Traverse: ", inorder_traverse(root))
```

