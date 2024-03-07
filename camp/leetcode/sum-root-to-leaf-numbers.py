# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preOrder(current, value):
            if not current:
                return 0
            value = 10*value + current.val
            if not current.left and not current.right:
                return value
            return preOrder(current.left, value) + preOrder(current.right, value)
           
        return preOrder(root, 0)
        