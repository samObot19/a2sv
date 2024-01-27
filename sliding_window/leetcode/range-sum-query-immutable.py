class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        running_sum = 0
        for i in range(len(nums)):
            nums[i] += running_sum
            running_sum = nums[i]
        self.nums = [0]+self.nums
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)