class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        #greedy
        max_num = nums[0]
        res = nums[0]

        for index in range(1, len(nums)):
            max_num += nums[index]
            res = max(res, ceil(max_num/(index + 1)))

        return res

        