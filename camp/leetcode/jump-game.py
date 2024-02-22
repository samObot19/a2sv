class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        i = 0
        while i < len(nums) - 1 and i <= reachable:
            reachable = max(reachable, nums[i] + i)
            if reachable >= len(nums) - 1:
                return True
            i += 1
            
        

        if len(nums) == 1:
            return True
        
        return False
        