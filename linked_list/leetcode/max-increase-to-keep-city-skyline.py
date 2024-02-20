class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_rows, max_cols, sky_line = [], [], 0
        for i in range(len(grid[0])):
            max_col = 0
            for j in range(len(grid)):      #calculating the maximum values for each columns
                max_col = max(max_col, grid[j][i])
            max_cols.append(max_col)
            
        for row in range(len(grid)):
            max_rows.append(max(grid[row]))  #calculating the maximum values for each rows

        
        for row in range(len(grid)):
            for col in range(len(grid)):
                current = grid[row][col]
                sky_line += max(current, min(max_rows[row], max_cols[col])) - current  #the greedy approch is here calculating the minimum of max_rows and max_cols
        
        return sky_line

                
        