class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s) + 1)
        new_str = []
        for shift in shifts:
            if shift[2] == 0:
                prefix[shift[0]] -= 1
                prefix[shift[1] + 1] += 1
            else:
                prefix[shift[0]] += 1
                prefix[shift[1] + 1] -= 1
       
        prefix = list(accumulate(prefix))
        for i in range(len(prefix) - 1):
            new_aski = (ord(s[i])- ord('a') + prefix[i] + 26)%26
            new_str.append(chr(ord('a') + new_aski))
        return "".join(new_str)
        