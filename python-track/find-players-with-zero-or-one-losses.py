class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counters = {}
        for i in matches:
            counters[i[0]] = 0
            counters[i[1]] = 0
            
        for i in matches:
            counters[i[1]] += 1

        lst = list(counters.keys())
        lst.sort()
        
        lst1 = [i for i in lst if counters[i] == 0]
        lst2 = [i for i in lst if counters[i] == 1]
        
        return [lst1, lst2]
        
        
        