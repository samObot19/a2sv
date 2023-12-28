class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        full = capacity
        steps= 0
        for i in range(len(plants)):
            if plants[i] > capacity:
                capacity = full
                steps += 2*i + 1
                capacity -= plants[i]
            else:
                capacity -= plants[i]
                steps += 1
         
        return steps