class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def search(index, temp):
            if index == len(nums):
                res.append(temp[:])
                return
            else:
                temp.append(nums[index])
                search(index + 1, temp)
                temp.pop()
                search(index + 1, temp)
        res = []
        search(0, [])
        return res