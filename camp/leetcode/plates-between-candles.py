class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum, ans = [], []
        for i in s:
            if i == '|':
                prefix_sum.append(0)
            else:
                prefix_sum.append(1)
        pre = [i for i in range(len(s)) if s[i] == '|']
        pre.append(10e6)
        prefix_sum = list(accumulate(prefix_sum))

        for start, end in queries:
            left_most = pre[bisect_left(pre, start)]
            right_most = pre[bisect_right(pre, end) - 1]
            if left_most>= right_most or right_most == 10e6:
                ans.append(0)
            else:
                ans.append(prefix_sum[right_most - 1] - prefix_sum[left_most])
        
        return ans

        