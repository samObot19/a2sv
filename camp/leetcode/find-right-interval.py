class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s = [start for start, end in intervals]
        starts = sorted(s)
        position = {value: index for index, value in enumerate(s)}
        ans = [-1 for i in range(len(intervals))]

        for index, (start, end) in enumerate(intervals):
            pos = bisect.bisect_left(starts, end)
            if pos != len(s):
                ans[index] = position[starts[pos]]

        return ans


        