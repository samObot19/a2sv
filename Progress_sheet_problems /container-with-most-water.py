class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while(left < right):
            Area = (right - left)*min(height[left], height[right])
            maxArea = max(maxArea, Area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea


        