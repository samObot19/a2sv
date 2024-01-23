class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, k - 1
        white, max_white = 0, 0
        #first stap counting the number of white
        for i in range(k):
            if blocks[i] == 'W':
                white += 1

        max_white = white
        #using fixed window size as an advantage excluding whites in left and including the right
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W':
                white -= 1
            max_white = min(white, max_white)
            
        return max_white