# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        def travel(p, q):
            nonlocal flag
            if not p and not q:
                return
            if (p and not q) or (not p and q):
                flag = False
                return
            
            if p.val != q.val:
                flag = False
            
            travel(p.left, q.left)
            travel(p.right, q.right)
    
        travel(p, q)
        return flag