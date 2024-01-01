class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if(matrix[i][j]!=matrix[i-1][j-1]):
                    return False
        return True
            