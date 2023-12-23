class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = [0 for i in range(len(s))]
        
        for index, value in enumerate(s):
            lst[indices[index]] = value
            
        s = ""
        for i in lst:
            s += i
            
        return s
        
        