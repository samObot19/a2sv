class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_right = Counter(nums)
        division_sum = defaultdict(lambda: [])
        q, p, k = 0, 0, 0
        division_sum[left_right[1]].append(0)
        max_division = left_right[1]

        for i in range(len(nums)):
            if left_right[0] > q and nums[i] == 0:
                count = i + left_right[1] - p + 1
                k = i + 1 - p
                #calculate the max value
                if count > max_division:
                    max_division = count
                division_sum[count].append(i + 1)
                q += 1
            else:
                left_right[1] -= 1
                p += 1
                count = k + left_right[1]
                if count > max_division:
                    max_division = count
                division_sum[count].append(i + 1)
            
        return division_sum[max_division]