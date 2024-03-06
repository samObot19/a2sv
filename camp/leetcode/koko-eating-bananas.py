class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, higher, best = 1, max(piles), 0

        while lower < higher:
            mid = lower + (higher - lower)//2
            counter = 0
            for i in range(len(piles)):
                counter += ceil(piles[i]/mid)
            
            if counter > h:
                lower = mid + 1 
            else:
                higher = mid

        
        return lower


        