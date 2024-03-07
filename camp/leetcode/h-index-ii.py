class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        N = len(citations)

        while left <= right:
            mid = left + (right - left)//2
            if citations[mid] < N - mid:
                left = mid + 1
            else:
                right = mid - 1
                

        return N - left
    

        