class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        dist = float('-inf')
        def min_distance(heater, house):
            left, right = 0, len(heater) - 1
            min_dist = float('inf')
            while left <= right:
                mid = left + (right - left)//2
                print
                min_dist = min(min_dist, abs(house - heaters[mid]))
                if heaters[mid] > house:
                    right = mid - 1
                else:
                    left = mid + 1
            return min_dist

        for house in houses:
            dist = max(dist, min_distance(heaters, house))

        return dist
        