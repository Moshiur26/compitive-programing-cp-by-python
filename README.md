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