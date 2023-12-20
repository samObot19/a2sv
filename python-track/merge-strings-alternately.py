class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        merged = ""
        
        i = 0
        j = 0
        
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged += word1[i]
            
                
            if j < len(word2):
                merged += word2[i]
        
                
            i = i + 1
            j = j + 1
                
        return merged
        