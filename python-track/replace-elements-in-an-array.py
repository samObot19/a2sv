class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashMap = {element: index for index, element in enumerate(nums)}
        for i in operations:
            nums[hashMap[i[0]]] = i[1]
            hashMap[i[1]] = hashMap[i[0]]
        
        return nums
        