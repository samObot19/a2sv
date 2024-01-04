class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        frequency = Counter(nums) #O(n)  m = number of unique elements
        unique_nums = list(set(nums)) #O(n) n = number of inputs
        #sort in reverse order O(m*log(m))
        unique_nums.sort(reverse=True)  
        operations, sum_of_operations = 0, 0
        #iterating the loop and calculating operations O(m)
        for i in range(0, len(unique_nums) - 1):
            operations = operations + frequency[unique_nums[i]]
            sum_of_operations += operations
            
        return sum_of_operations
