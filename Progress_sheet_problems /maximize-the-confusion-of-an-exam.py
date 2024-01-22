class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def confusion(ans, c, n):
            i, j = 0, 0
            while j < len(ans):
                if ans[j] == c:
                    n -= 1
                if n < 0:
                    if ans[i] == c:
                        n += 1
                    i += 1
                j += 1

            return j - i

        return max(confusion(answerKey, 'T', k), confusion(answerKey, 'F', k))
        