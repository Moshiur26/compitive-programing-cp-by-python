from binaryTreeNode import BinaryTreeNode


def inorder_traversal(tree):
  if tree:
    inorder_traversal(tree.left)
    print(tree.data, end=' ')
    inorder_traversal(tree.right)


def preorder_traversal(tree):
  if tree:
    print(tree.data, end=' ')
    preorder_traversal(tree.left)
    preorder_traversal(tree.right)


def postorder_traversal(tree):
  if tree:
    postorder_traversal(tree.left)
    postorder_traversal(tree.right)
    print(tree.data, end=' ')


root = BinaryTreeNode(8)
root.left = BinaryTreeNode(4)
root.right = BinaryTreeNode(5)

root.left.left = BinaryTreeNode(344)
root.left.right = BinaryTreeNode(42)
root.right.left = BinaryTreeNode(32)
root.right.right = BinaryTreeNode(53)

root.left.left.left = BinaryTreeNode(344)
root.left.left.right = BinaryTreeNode(344)
root.left.right.left = BinaryTreeNode(42)
root.left.right.right = BinaryTreeNode(24)
root.right.left.left = BinaryTreeNode(32)
root.right.left.right = BinaryTreeNode(43)
root.right.right.left = BinaryTreeNode(53)
root.right.right.right = BinaryTreeNode(23)

print('Inorder: ', end=' ')
inorder_traversal(root)

print('\nPreorder:', end=' ')
preorder_traversal(root)

print('\nPostorder', end=' ')
postorder_traversal(root)
