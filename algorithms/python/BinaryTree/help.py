# preorder
#    1
#  2   3
def preorderTraversal(self, root: TreeNode) -> List[int]:
    result = []
    stack = []

    while root is not None or 0 < len(stack):
        if root is not None:
            stack.append(root)
            result.append(root.val)  # left is first
            root = root.left
        else:
            root = stack.pop()
            root = root.right

    return result

# preorder -> postorder + reverse
#    1            1          3
#  2   3        3   2      1   2
def postorderTraversal(self, root: TreeNode) -> List[int]:
    result = []
    stack = []

    while root is not None or 0 < len(stack):
        if root is not None:
            stack.append(root)
            result.append(root.val)  #right is first
            root = root.right
        else:
            root = stack.pop()
            root = root.left

    return result[::-1]  # reverse

def inorderTraversal(self, root: TreeNode) -> List[int]:
    result = []
    stack = []

    while root is not None or 0 < len(stack):
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root.val)  # left has gone
            root = root.right

    return result