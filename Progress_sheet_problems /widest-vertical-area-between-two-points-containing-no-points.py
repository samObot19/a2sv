class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        lst = [x for x, y in points]
        lst.sort()
        maxWidth = 0

        for i in range(1, len(lst)):
            current = lst[i] - lst[i - 1]
            maxWidth = max(maxWidth, current)

        return maxWidth