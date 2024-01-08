class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        n = len(nums)
        while i < n:
            if nums[i] - nums[i - 1] != 0: #replacing duplicate element by unique one
                nums[j] = nums[i]
                j += 1
            i += 1
        return j