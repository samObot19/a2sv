class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0] + list(accumulate(nums)) #calculating prefix sum

        for i in range(len(nums)):  #chaking the left and right sums of each inex
            if prefix[i] == prefix[-1] - prefix[i + 1]: #is there are equals return that index 
                return i
        
        return -1