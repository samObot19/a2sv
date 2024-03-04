class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        #use the test case first->
        #[1, 3, 5, 1]  we must divide in two bag b/c k = 2
        #[1, 3, 5, 1]  the sum of the first element and the last = 1 + 1 = 2
        #1->[1], [3, 5, 1]  sum = ("1" + 1) + (3 + "1") = 2 + (3 + 1)   
        #2->[1, 3] [5, 1]   sum = ("1" + 3) + (5 + "1") = 2 + (3 + 5)
        #3->[1, 3, 5] [1]   sum = ("1" + 5) + (1 + "1") = 2 + (5 + 1)
        #in this three pattern the sum of the first and the last element of the weights are constant 
        #so we can take the minimum pair sum and maximum pair sum
        #min = (3 + 1) and max = (5 + 3)
        #the answer will be ans = 8 - 4 = 4

        pairs = []
        for i in range(len(weights) - 1):
            pairs.append(weights[i] + weights[i + 1])

        
        pairs.sort()
        
        n,  _min, _max = len(pairs) - 1, 0, 0
        for i in range(k - 1):
            _max += pairs[n - i]
            _min += pairs[i]
        
        return _max - _min
        