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
