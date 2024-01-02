class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            lst = []
            for j in range(len(matrix)):
                lst.append(0)
            transpose.append(lst)
                
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                    transpose[j][i] = matrix[i][j]
        
        return transpose