class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        cnt = defaultdict(int) # tracking  the frequency of the character at maximum the size is 2 its O(1) space complexity
        res, left = 0, 0  # the max_length and the left pointer
        
        for i in range(N):
            cnt[fruits[i]] += 1

            while len(cnt) > 2: #removing element tha occure more than 2 times and shrinking the window size
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1            
            
            res = max(res, i - left + 1) # tracking the maximum size of the window

        return res