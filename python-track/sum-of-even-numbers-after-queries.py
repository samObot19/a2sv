class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sums = sum([i for i in nums if i % 2 == 0])
        
        for [value, index] in queries:
            val = nums[index]
            nums[index] += value
            
            if val % 2 == 0:
                sums -= val
            if nums[index] % 2 == 0:
                sums += nums[index]
                
            result.append(sums)
            
        return result
            
        