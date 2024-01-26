class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = defaultdict(lambda: 0)
        freq[0] = 1
        s, ans = 0, 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        for i in range(len(nums)):
            s += nums[i]
            if freq[s - k] > 0:
                ans += freq[s - k]
            freq[s] += 1
        return ans

        
            
