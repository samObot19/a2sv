class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        one_third = len(nums)//3
        dic = {}
        
        for i in nums:
            dic[i] = 0
            
            
        for i in nums:
            dic[i] += 1
        ans = []
        for i in dic:
            if (dic[i] > one_third):
                ans.append(i)
                
        return ans
            
            