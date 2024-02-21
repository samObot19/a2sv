class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while right > left:
                if nums[left] + nums[right] > nums[i]:
                    s += (right - left)
                    right -= 1
                else:
                    left += 1

        return s
              
