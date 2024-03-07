class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def combination(j, List):
            if len(List) == k:
                result.append(List[:])
                return
            
            for i in range(j, n + 1):
                List.append(i)
                combination(i + 1, List)
                List.pop()
               
        combination(1, [])  
        return result      
