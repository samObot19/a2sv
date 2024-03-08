class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        lower = bisect_left(nums, target)
        higher = bisect_right(nums, target)
        if not N:
            return[-1, -1]
        if lower < N and nums[lower] == target:
            return [lower, higher - 1]
        
        return [-1, -1]