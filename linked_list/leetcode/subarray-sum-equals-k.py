class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        frequency[0] += 1
        s, ans = 0, 0

        for i in nums:
            s += i
            diff = s - k
            if diff in frequency:
                ans += frequency[diff]
            frequency[s] += 1

        return ans
        