class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        lst = [0 for i in range(len(words))]

        for word in words:
            index = int(word[len(word) - 1]) - 1
            lst[index] = word[: len(word) - 1]

        return " ".join(lst)


        