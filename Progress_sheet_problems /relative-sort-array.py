class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {value: index for index, value in enumerate(arr2)}
        n = [i for i in arr1 if i in order]
        m = [i for i in arr1 if not i in order] 
        m.sort()       
        return sorted(n, key=lambda x: order[x]) + m
       
            
        