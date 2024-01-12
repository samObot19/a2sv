class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for i in s:
            if i.isalnum():
                lst.append(i)
        s = "".join(lst).lower()
        return s == s[::-1]