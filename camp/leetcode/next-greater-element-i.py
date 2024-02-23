class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = defaultdict(lambda:-1) #to keep track the next greater element of all elements in nums2
        stack = []

        for val in nums2:
            while stack and val > stack[-1]:
                k = stack.pop()
                next_greater[k] = val
            stack.append(val)

        for i in range(len(nums1)): #inserting the next greater element in the subset of nums2 
            nums1[i] = next_greater[nums1[i]]

        return nums1