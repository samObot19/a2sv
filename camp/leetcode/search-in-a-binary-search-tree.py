# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node, val):
            if not node:
                return None
            if node.val < val:
                return search(node.right, val)
            elif node.val > val:
                return search(node.left, val)
            else:
                return node

        root = search(root, val)
        return root