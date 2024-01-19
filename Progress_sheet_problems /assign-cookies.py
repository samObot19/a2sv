class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        ans = 0
        
        i, j = 0, 0
        g.sort(reverse = True)
        s.sort(reverse = True)
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
                j += 1
            else:
                i+=1
                
        return ans
            
        