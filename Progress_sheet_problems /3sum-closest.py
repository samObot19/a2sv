class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minimum, length = float("inf"), len(nums)
        nums.sort()

        for index in range(length):
            left, right = index + 1, length - 1
            while left < right:
                threeSum = nums[index] + nums[left] + nums[right]
                if  threeSum < target:
                    left += 1
                else:
                    right -= 1
                if abs(minimum - target) > abs(threeSum - target):
                    minimum = threeSum
        
        return minimum

