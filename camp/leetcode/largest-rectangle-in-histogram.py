class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        position, bars = [],[]
        max_area, N = 0, len(heights)

        for pos in range(len(heights)):
            index = pos

            while bars and bars[-1] > heights[pos]:
                index = position.pop()
                height = bars.pop()
                max_area = max(max_area, (pos - index)*height)

            bars.append(heights[pos])
            position.append(index)

       
        while bars:
            width = N - position.pop()
            height = bars.pop()
            max_area = max(max_area, height * width)
    
        return max_area
        
        