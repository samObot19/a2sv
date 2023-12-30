class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        Ord = [0 for i in range(len(order))]
        
        for i in range(len(order)):
            Ord[ord(order[i]) - ord('a')] = i
            
        for i in range(len(words) - 1):
            Curr = words[i]
            Next = words[i + 1]
            
            length = min(len(Curr), len(Next))
            if len(Curr) != length and len(Next) == length and Curr.startswith(Next):
                return False
            
            for j in range(length):
                if Ord[ord(Curr[j]) - ord('a')] > Ord[ord(Next[j]) - ord('a')]:
                    return False
                
                if Ord[ord(Curr[j]) - ord('a')] < Ord[ord(Next[j]) - ord('a')]:
                    break
        
        
        return True