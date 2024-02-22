class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-1 for i in range(len(nums))]
        N = len(nums)
        stack = []

        for index in range(N*2):#iterating 2 times b/c of the next greater element is circular manner
            while stack and nums[index % N] > nums[stack[-1]]:
                i = stack.pop()
                answer[i % N] = nums[index % N]
            stack.append(index % N)        

        return answer