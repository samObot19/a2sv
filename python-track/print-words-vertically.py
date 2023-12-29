class Solution:
    def printVertically(self, s: str) -> List[str]:
        hashMap = defaultdict(lambda:"")
        words = s.split()
        max_len = max([len(word) for word in words])
        
        for word in words:
            for i in range(max_len):
                if i >= len(word):
                    hashMap[i] += " "
                else:
                    hashMap[i] += word[i]
                    
        ans = [i.rstrip() for i in hashMap.values()]
            
        return ans
        