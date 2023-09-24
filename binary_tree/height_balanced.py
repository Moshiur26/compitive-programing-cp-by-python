import collections
from binaryTreeNode import BinaryTreeNode


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

