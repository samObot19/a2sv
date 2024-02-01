class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0 for i in range(len(nums) + 1)]
        max_sum = 0
        mod = 10**9 + 7
        for left, right in requests:
            prefix[left] += 1
            prefix[right + 1] -= 1

        prefix = sorted(accumulate(prefix), reverse=True)
        nums.sort(reverse=True)
        for i in range(len(nums)):
            max_sum += nums[i]*prefix[i]

        return max_sum % mod
    
        