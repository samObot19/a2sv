class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter = sorted(list(set(letters)))
        
        N = len(letters)
        i = bisect_right(letters, target)
        if i != N:
            return letters[i]

        return letters[0]