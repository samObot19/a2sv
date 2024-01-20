class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        j, vow, max_vowels = k, 0, 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        for i in range(k):
            if s[i] in vowels:
                vow += 1
                max_vowels += 1
        while j < len(s):
            if s[j] in vowels:
                vow += 1
            if s[j - k] in vowels:
                vow -= 1
            max_vowels = max(max_vowels, vow)
            j += 1
        return max_vowels
        