class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j, k = 0, 0, 1
        while i < len(nums):
            if nums[i] == 0:
                k -= 1 
            if k < 0:
                if nums[j] == 0:
                    k += 1
                j += 1
            i += 1

        return i - j - 1
        