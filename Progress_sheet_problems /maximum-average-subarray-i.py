class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        j = k
        max_average = sum(nums[:k])
        average = sum(nums[:k])
        while j < len(nums):
            average += nums[j] - nums[j - k]
            max_average = max(max_average, average)
            j += 1
        return max_average/k
            
        