class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        answer = [0 for i in range(len(temperatures))]

        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]: #kick out the smaller elements from the stack
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        
        return answer
        