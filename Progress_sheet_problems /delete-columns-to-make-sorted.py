class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(1 for col in zip(*strs) if list(col) !=sorted(col))
        