class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lst = []
        if num % 3 == 0:
            intial = num/3 - 1
            num2 = intial + 1
            num3 = intial + 2
            lst.append(intial)
            lst.append(num2)
            lst.append(num3)
        
        return lst