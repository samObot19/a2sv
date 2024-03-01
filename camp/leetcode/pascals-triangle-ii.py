class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal_triangle(n):
            if n == 0:
                return [1]
            if n == 1:
                return [1, 1]
            else:
                current_row = [1]
                prev_row = pascal_triangle(n - 1)
                for i in range(1, len(prev_row)):
                    current_row.append(prev_row[i-1] + prev_row[i])
                current_row.append(1)
                return current_row
        
        return pascal_triangle(rowIndex)
        



        