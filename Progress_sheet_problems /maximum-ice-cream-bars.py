class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_cream = 0
        for i in costs:
            if i <= coins:
                ice_cream += 1
                coins -= i
        
        return ice_cream
        