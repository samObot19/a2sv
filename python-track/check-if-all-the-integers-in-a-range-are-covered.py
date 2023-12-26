class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sets = set()
        for i in ranges:
            sets.update([j for j in range(i[0], i[1] + 1)])
            
        set2 = set([i for i in range(left, right + 1)])
        
        return set2 <= sets
        
        
            
        