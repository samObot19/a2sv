class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = defaultdict(lambda:0)
        left, right = 0, 0
        _sum, _max = 0, 0

        while right < len(nums):
            _sum += nums[right]
            freq[nums[right]] += 1
            while freq[nums[right]] > 1:
                freq[nums[left]] -= 1
                _sum -= nums[left]
                left += 1
            _max = max(_sum, _max)
            right += 1
        
        return _max

        