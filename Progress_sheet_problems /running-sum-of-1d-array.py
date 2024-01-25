class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0

        for i in range(len(nums)):
            nums[i] += running_sum
            running_sum = nums[i]

        return nums