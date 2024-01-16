class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        Max = float(-inf)
        for row in range(len(grid) - 2):
            for col in range(len(grid[row]) - 2):
                current = (grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
                + grid[row + 1][col + 1]
                + grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2])
                #window in fixed hour glass
                Max = max(Max, current)
        return Max

        