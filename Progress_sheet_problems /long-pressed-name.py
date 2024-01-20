class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, N, T = 0, 0, len(name), len(typed)
        while j < T:
            if i < N and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
        return i == N