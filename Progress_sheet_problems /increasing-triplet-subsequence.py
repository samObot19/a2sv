class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True     #if there is the number greater than both first and second it gareenty that the nums array have increasing triplate sequence 
        return False