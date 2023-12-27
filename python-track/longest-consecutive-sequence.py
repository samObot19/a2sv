class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        Max = 1
        if (len(nums) == 0):
            return 0
        for i in range(1, len(nums)):
            if (nums[i - 1] + 1 == nums[i]):
                print(count)
                count += 1
            elif nums[i - 1] == nums[i]:
                continue
            else:
                print(count)
                count = 1
           
            if count > Max:
                Max = count
              
                    
        if(count > Max):
            Max = count
        
        
        return Max