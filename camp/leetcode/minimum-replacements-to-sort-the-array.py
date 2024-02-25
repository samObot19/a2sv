class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                number_of_elements = ceil(nums[i]/nums[i+1])
                answer += number_of_elements - 1
                nums[i] = nums[i]//number_of_elements

        return answer