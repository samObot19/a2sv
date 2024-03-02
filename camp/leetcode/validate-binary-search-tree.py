# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        def inorder(current):
            nonlocal values
            if not current:
                return
            inorder(current.left)
            values.append(current.val)
            inorder(current.right)
    
        inorder(root)
        isBst = True

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                isBst = False
        return isBst