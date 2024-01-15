class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        order = {}
        n = [i for i in nums]
        nums.sort()
        for i in range(len(nums)):
            order[nums[i]] = i + 1 - frequency[nums[i]]

        for i in range(len(n)):
            n[i] = order[n[i]]

        return  n

