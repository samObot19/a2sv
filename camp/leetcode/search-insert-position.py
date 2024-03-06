class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high, best = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] < target:
                low = mid + 1
                best = low
            elif nums[mid] > target:
                high = mid - 1
                best = mid
            else:
                return mid
            

        return best
        