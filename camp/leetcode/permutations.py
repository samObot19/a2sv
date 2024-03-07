class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(index):
            if index == len(nums):
                answer.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permutation(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        
        answer = []
        permutation(0)
        return answer
