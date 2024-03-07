class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False
        def helper(row, col, i, visited):
            if (row, col) in visited:
                return False
            if board[row][col] != word[i]:
                return False
            if i == len(word) - 1 and board[row][col] == word[i]:
                return True
            visited.add((row, col))
            up = helper(row - 1, col, i + 1, visited.copy()) if row > 0 else False
            down = helper(row + 1, col, i + 1, visited.copy()) if row < len(board) - 1 else False
            left = helper(row, col - 1, i + 1, visited.copy()) if col > 0 else False
            right = helper(row, col + 1, i + 1, visited.copy()) if col < len(board[0]) - 1 else False
            return up or down or left or right
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = helper(i, j, 0, set())
                    if temp:
                        return True
        return False
        

        