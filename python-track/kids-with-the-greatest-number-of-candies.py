class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        maximum = max(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                lst.append(True)
            else:
                lst.append(False)
                
                
        return lst