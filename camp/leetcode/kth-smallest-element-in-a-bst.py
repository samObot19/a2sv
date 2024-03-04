# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = 0
        def inorder(current, k):
            nonlocal val, i
            if not current:
                return 
            inorder(current.left , k)
            i += 1
            if i == k:
                val = current.val
                return
            inorder(current.right , k)
        
        i = 0
        inorder(root, k)
        return val