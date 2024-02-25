class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                distance = i - stack[-1] - 1 #calculating the distance b/n the traps
                bounded_height = min(height[i], height[stack[-1]]) - height[top] #the height boundary b/n the middle and the minimum height b/n the two traps
                water += distance * bounded_height #increament the amount of traped water by the area covered by the distance b/n the two traps and height

            stack.append(i)

        return water