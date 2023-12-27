class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        ans = []
        
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in hashMap:
                ans.append(i)
                ans.append(hashMap[difference])
                break
            else:
                hashMap[nums[i]] = i
                
        
        return ans