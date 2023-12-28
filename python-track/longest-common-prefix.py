class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst = sorted(strs)
        ans = []
        
        first = lst[0]
        last = lst[-1]
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return "".join(ans)
            
            ans.append(first[i])
            
        return "".join(ans)