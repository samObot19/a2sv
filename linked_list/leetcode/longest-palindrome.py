class Solution:
    def longestPalindrome(self, s: str) -> int:
        N = len(s)
        freq = Counter(s)
        p = 0

        for val in freq.values():
            if val % 2 == 0:
                p += val
            else:
                p += val - 1


        return p + 1 if N - p else p
        