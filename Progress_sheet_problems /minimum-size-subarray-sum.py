class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_length = float('inf')
        total = 0

        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_length = min(min_length, right - left + 1)   #decreasing the window size when the total is greater than the target value
                total -= nums[left]
                left += 1
            right += 1 

        return 0 if min_length == float('inf') else min_length
                