class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        _end = len(cardPoints)
        curr_sum = _max = sum(cardPoints[:k]) #taking the sum of the first k windows

        for i in range(k-1, -1, -1):
            curr_sum -= cardPoints[i] #taking the current_sum by decrementing the intial window
            curr_sum += cardPoints[_end - k + i] #increamenting the end elements or including the last eindow
            _max = max(_max, curr_sum) #talking the maximum sum window

        return _max



