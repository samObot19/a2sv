class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        left, right = 0, 0
        optimal_time = 0
        while right < len(tasks):
            current_time = tasks[right] + processorTime[left]
            optimal_time = max(current_time, optimal_time)
            left += 1
            right += 4

        return optimal_time

        