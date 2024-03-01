# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val == right.val and Check(left.left, right.right) and Check(left.right, right.left)

        return Check(root.left, root.right)
        