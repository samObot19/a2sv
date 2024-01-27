class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = defaultdict(lambda: 0)
        freq[0] = 1
        s, ans = 0, 0

        for i in range(len(nums)):
            s += nums[i]
            if freq[s - goal] > 0:
                ans += freq[s - goal]
            freq[s] += 1
        return ans


