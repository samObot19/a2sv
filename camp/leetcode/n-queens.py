class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        col = set()
        pos_digo = set()
        neg_digo = set()
        ans = []
        def back_tracking(k):
            if k == n:
                temp = [''.join(i) for i in board]
                x = deepcopy(temp)
                ans.append(x)
                return
            
            for i in range(n):
                if i in col or i + k in pos_digo or i - k in neg_digo:
                    continue
                
                board[k][i] = 'Q'
                col.add(i)
                pos_digo.add(i + k)
                neg_digo.add(i - k)

                back_tracking(k + 1)

                board[k][i] = '.'
                col.remove(i)
                pos_digo.remove(i + k)
                neg_digo.remove(i - k)

        back_tracking(0)
        return ans
        