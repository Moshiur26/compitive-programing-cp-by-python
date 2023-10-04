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
print('Tree LCA: %d' % result.data)
