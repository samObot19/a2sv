# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def maximum_number_index(left, right):
            return nums.index(max(nums[left: right + 1]))
        def maxBT(node, left, right):
            if left > right:
                return None
            i = maximum_number_index(left, right)
            root = TreeNode(nums[i])
            root.left = maxBT(root, left, i - 1)
            root.right = maxBT(root, i + 1, right)
            return root
        return maxBT(TreeNode(), 0, len(nums) - 1)

        