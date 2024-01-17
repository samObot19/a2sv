class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        current, total = 0, 0

        for i in range(len(flips)):
            current += flips[i]
            blues = (i + 1)*(i + 2)//2
            if blues == current:
                total += 1
        #O(1) --- space
        #O(n) ---- time complexity

        return total
        