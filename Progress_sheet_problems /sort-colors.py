class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3
        for num in nums:
            freq[num] += 1

        for i in range(freq[0]):
            nums[i] = 0
        
        for i in range(freq[0], freq[1] + freq[0]):
            nums[i] = 1
        
        for i in range(freq[1] + freq[0], len(nums)):
            nums[i] = 2

        return nums
        