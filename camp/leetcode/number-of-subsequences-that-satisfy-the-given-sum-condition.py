class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        left, right = 0, len(nums) - 1
        sub_sequence = 0
        for i in range(len(nums)):
            while nums[left] + nums[right] > target and left <= right:
                right -= 1
            
            if left <= right:
                sub_sequence += pow(2, right - left, MOD)
            left += 1

        return sub_sequence%MOD
        