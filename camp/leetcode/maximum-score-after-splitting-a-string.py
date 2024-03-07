class Solution:
    def maxScore(self, s: str) -> int:
        total = 0
        prefix = [0]
        for  i in range(len(s)):
            prefix.append(prefix[-1] + int(s[i]))
            total += int(s[i])
        
        res = 0

        for i in range(1, len(s)):
            res = max(res, total - 2*prefix[i] + i)

        return res