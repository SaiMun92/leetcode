class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node: 
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret


        # method 2 - preferred
        def preorderTraversal(self, root):
            res, stack = [], []
            while root or stack:
                # traversing the root by left and then right
                if root:
                    res += root.val,
                    stack += root.right, root.left,
                root = stack.pop()
            return res  