# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_difference = 0
        def Max_difference(Min, Max, current):
            nonlocal max_difference
            if not current:
                return
            max_difference = max(max_difference, max(abs(current.val - Min), abs(Max - current.val)))
            Min = min(Min, current.val) 
            Max = max(Max, current.val)
            Max_difference(Min, Max, current.left)
            Max_difference(Min, Max, current.right)

        Min = Max = root.val
        Max_difference(Min, Max, root)
        return max_difference
        