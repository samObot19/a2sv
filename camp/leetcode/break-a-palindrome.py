class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        lst = [i for i in palindrome]
        N = len(lst)
        i, j = 0, N - 1
        if N == 1: return ""

        while i < j:
            if lst[i] > 'a':
                lst[i] = 'a'
                return "".join(lst)
            i += 1
            j -= 1

        lst[N - 1] = 'b'
        return "".join(lst)

        