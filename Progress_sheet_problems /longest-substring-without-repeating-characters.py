class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurrence = defaultdict(lambda: 0)
        left, right, count = 0, 0, 0

        while right < len(s):
            if occurrence[s[right]] == 0:
                occurrence[s[right]] += 1
                right += 1
                count = max(count, right - left)
            else:
                occurrence[s[left]] -= 1
                left += 1

        return count