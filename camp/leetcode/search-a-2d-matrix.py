class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            low, high = 0, len(m) - 1
            while low <= high:
                mid = (high + low) // 2
                if m[mid] < target:
                    low = mid + 1
                elif m[mid] > target:
                    high = mid - 1
                else:
                    return True

        return False
 