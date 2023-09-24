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
