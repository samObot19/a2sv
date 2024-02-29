# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        ans = []

        def preorder(row, col, node):
            nonlocal cols
            if not node:
                return
                
            cols[col].append((row, node.val))
            preorder(row + 1, col - 1, node.left)
            preorder(row + 1, col + 1, node.right)

        preorder(0, 0, root)

        for col in sorted(cols):
            ans.append([val for _, val in sorted(cols[col])])
        return ans

        