class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst = []
        negative = []
        for i in nums:
            if i > 0:
                lst.append(i)
                lst.append(0)
            else:
                negative.append(i)
                
        i = 0
        
        for index in range(len(lst)):
            if lst[index] == 0:
                lst[index] = negative[i]
                i += 1
                
        return lst