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
