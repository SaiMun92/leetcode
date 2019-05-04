class Solution:
  def inorderTraversal(self, root):
      ans = []
      stack = []
      
      while stack or root:
          # keep going to the left and append the root to the stack
          if root:
              stack.append(root)
              root = root.left
          # pop the stack and append the values to the ans
          else:
              tmpNode = stack.pop()
              ans.append(tmpNode.val)
              root = tmpNode.right
          
      return ans