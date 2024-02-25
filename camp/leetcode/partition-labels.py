class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = [-1 for i in range(26)] #it store the last occurence of each character
        answer, ends, k = [], 0, 0
        for end in range(len(s)): #iterating to get the last occurence of each character of string
            last_occur[ord(s[end]) - ord('a')] = end

        
        for i in range(len(s)):
            ends = max(ends, last_occur[ord(s[i]) - ord('a')]) #iterating throw the string characters taking the the max index occurence of each character as long as  equal to the current index 
            k += 1
            if ends == i:
                answer.append(k)
                k = 0

        return answer
        
        