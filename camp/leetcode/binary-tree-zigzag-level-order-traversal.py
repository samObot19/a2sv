# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rows = defaultdict(list)
        answer = []
        def Zig(current, row):
            if not current:
                return

            rows[row].append(current.val)
            Zig(current.left, row + 1)
            Zig(current.right, row + 1)
        
        Zig(root, 0)
        for i in range(len(rows)):
            if i % 2:
                answer.append(reversed(rows[i]))
            else:
                answer.append(rows[i])

        return answer

        