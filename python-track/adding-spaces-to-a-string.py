class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = s[:spaces[0]]
        
        for i in range(len(spaces) - 1):
            string += " " + s[spaces[i] : spaces[i + 1]]
            
        string += " " + s[spaces[len(spaces) - 1]:]
        return string