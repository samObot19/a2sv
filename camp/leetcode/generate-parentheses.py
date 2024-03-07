class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backTrack(n, openp, closep, temp):
            if openp == closep and openp == n and closep == n:
                ans.append("".join(temp[:]))
                return
            if openp < n:
                temp.append('(')
                backTrack(n, openp + 1, closep, temp)
                temp.pop()
            if closep < openp:
                temp.append(')')
                backTrack(n, openp, closep + 1, temp)
                temp.pop()

        ans = []
        backTrack(n, 0, 0, [])
        return ans

        