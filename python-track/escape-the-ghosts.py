class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mnt_distance = []
        distance = abs(target[1]) + abs(target[0])

        
        for i in ghosts:
            if distance >= (abs(i[0]-target[0]) + abs(i[1]-target[1])):
                return False
            
        return True
            
                
        