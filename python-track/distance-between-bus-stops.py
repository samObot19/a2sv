class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sums = sum(distance)
        clockWise = 0
        if start > destination:
            start, destination = destination, start
        
        while(start != destination):
            clockWise += distance[start]
            start += 1
        return (min(clockWise, sums - clockWise))
        
        
            
        
            
            