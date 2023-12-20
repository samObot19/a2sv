class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
    
        """
        
        while(n != 0):
            remender = n % 3
            if remender == 2:
                return False
            n = n//3
            
        return True
            