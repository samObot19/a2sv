class Solution:
    def check(self, lst1, lst2):
        for i in range(26):
            if lst1[i] != lst2[i]:
                return False
        return True


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        frequency = [0 for i in range(26)]
        frequency2 = [0 for i in range(26)]
        size = len(s1)

        for ch in s1:
            frequency[ord(ch) - ord('a')] += 1

        for i in range(len(s1)):
            frequency2[ord(s2[i]) - ord('a')] += 1 #count the occurance of the the intial window

        if self.check(frequency, frequency2):#check if is permutation
            return True

        for r in range(size, len(s2)):
            frequency2[ord(s2[r]) - ord('a')] += 1  #includeing the next element
            frequency2[ord(s2[r - size]) - ord('a')] -= 1 #excluding the previous one
            if self.check(frequency, frequency2): #check is a permutation
                return True

        return False 
            


        




        