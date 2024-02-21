class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # First, sort the array of balloons based on their end positions in ascending order.
        points = sorted(points, key=lambda x : x[1])
        arrows = len(points)
        prev = points[0][1]
        for i in range(1, len(points)):
            if prev >= points[i][0]:
                arrows -= 1
            else:
                prev = points[i][1]
                
        return arrows