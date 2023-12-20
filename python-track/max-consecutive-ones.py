class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        Max = 0
        count = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                count = count + 1;
                if(Max < count):
                    Max = count
            else:
                count = 0
            
        return Max
        