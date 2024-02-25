class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #how much cost reduced if the person goes to city A
        #example if the costs = [[a, b], [c, d]]
        #first all person goto city A => (a + c)
        #after that taking the cost difference b/n each city cost [b - a, c- d]
        #if b - a < c - d  its prefered the first go to city b
        # (a + c) + (b - a) implies that the selcted costs are b for the first person
        #and c for the seond one by implementing this greedy approche. 
        min_cost = 0
        reduced = []

        for a, b in costs:
            reduced.append(b - a) 
            min_cost += a

        reduced.sort()

        for i in range(len(reduced)//2):
            min_cost += reduced[i]

        return min_cost

        