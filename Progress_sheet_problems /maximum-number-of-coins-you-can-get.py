class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        constant = len(piles) - len(piles)//3  
        return sum(piles[1:constant:2])
        
        