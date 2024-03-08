class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)

        left, right = max(nums), sum(nums)
        while left <= right :
            mid = ( left + right ) // 2
            summ = 0
            splits = 1
            for i in nums:
                summ += i
                if summ <= mid:
                    continue
                else:
                    splits += 1
                    summ = i
            
            if splits > k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

        