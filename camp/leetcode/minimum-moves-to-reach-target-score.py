class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        #using greedy approch 
        #starting from the target number if  maxDoubles  available back to the half stapes otherwise back to one step
        steps = 0

        while target != 1:
            if maxDoubles > 0:
                steps += target % 2 + 1
                target = target//2
                maxDoubles -= 1
            else:
                steps += target - 1
                target = 1
            
        return steps
