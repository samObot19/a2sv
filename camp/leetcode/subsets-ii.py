class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        isduplicate = set()

        def search(k, temp):
            if k == len(nums):
                c = sorted(temp)
                if (tuple(c)) not in isduplicate:
                    ans.append(temp[:])
                    isduplicate.add(tuple(c))
                return
            else:
                temp.append(nums[k])
                search(k + 1, temp)
                temp.pop()
                search(k + 1, temp)
        ans = []
        search(0, [])
        return ans
                
        