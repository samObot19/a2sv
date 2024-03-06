class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while True:
            mid = low + (high - low)//2
            if mid*mid <= x < (mid + 1)*(mid + 1):
                return mid
            elif x < mid*mid:
                high = mid - 1
            else:
                low = mid + 1

        