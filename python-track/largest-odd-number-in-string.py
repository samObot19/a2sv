class Solution:
    def largestOddNumber(self, num: str) -> str:
        lastOddIndex = len(num) - 1
        
        while lastOddIndex >= 0:
            if int(num[lastOddIndex]) % 2 != 0:
                return num[: lastOddIndex + 1]
            lastOddIndex -= 1
            
        return ""