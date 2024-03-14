class Solution:
    def balancedString(self, s: str) -> int:
        def isbalanced(freq, target):
            return max(freq.values()) <= target

        freq = Counter(s)
        N, left = len(s), 0
        minlen = N
        target = N//4

        if isbalanced(freq, target):
            return 0

        for r in range(N):
            freq[s[r]] -= 1
            while left < N and isbalanced(freq, target):
                minlen = min(minlen, r - left + 1)
                freq[s[left]] += 1
                left += 1
                    
        return minlen



        
        