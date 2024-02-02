class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0 for i in range(26)]
        max_len, left = 0, 0

        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1

            if right - left + 1 - max(freq) > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)


        return max_len