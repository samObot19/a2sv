class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        num = x
        reversed = 0
        while num != 0:
            digit = num % 10;
            reversed = reversed * 10 + digit;
            num = num // 10
            
        return reversed == x

        
        
        