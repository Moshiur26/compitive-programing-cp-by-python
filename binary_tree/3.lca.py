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
