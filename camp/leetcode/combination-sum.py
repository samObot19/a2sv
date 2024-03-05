class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        exist = set()
        def backTrack(sums, index, path):
            if sums > target:
                return
            if sums == target:
                c = sorted(path)
                if tuple(c) not in exist:
                    combs.append(path[:])
                    exist.add(tuple(c))
                return
        
            for i in range(len(candidates)):
                path.append(candidates[i])
                backTrack(sums + candidates[i], index + 1, path)
                path.pop()
               

        combs = []
        backTrack(0, 0, [])
        return combs

        