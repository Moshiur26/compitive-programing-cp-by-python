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
