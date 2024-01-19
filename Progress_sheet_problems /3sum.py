class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length, ans = len(nums), []

        for index in range(length):
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            left, right = index + 1, length - 1
            while left < right:
                if nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[index] < 0:
                    left += 1
                else:
                    ans.append([nums[left], nums[right], nums[index]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                

        return ans

        