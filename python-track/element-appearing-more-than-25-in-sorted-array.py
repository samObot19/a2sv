class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        frequency = len(arr) // 4
        count = 0
        
        for i in range(len(arr) - frequency):
            if arr[i] == arr[i + frequency]:
                return arr[i]
                
        
        return -1