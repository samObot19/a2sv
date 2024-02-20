class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers) # calculating how many rabbits have the same number of colors
        ans = 0
        for rabbit, values in freq.items():
            ans += (rabbit + 1)*ceil(values / (rabbit + 1))
    
        return ans
