class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        number_of_pairs = 0
        for i in frequency.values():
            if i >= 2:
                number_of_pairs += math.factorial(i)//(math.factorial(i - 2)* 2)
            
        return number_of_pairs