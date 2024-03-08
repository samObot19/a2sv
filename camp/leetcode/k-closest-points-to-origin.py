class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance, ans = [], []

        for x, y in points:
            distance.append([sqrt(x**2 + y**2), x, y])

        distance.sort()
        for i in range(k):
            ans.append([distance[i][1], distance[i][2]])
        return ans
