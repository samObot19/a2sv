class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numbers = map(str, digits)
        num = int("".join(numbers)) + 1
        num_str = str(num)
        plus = [i for i in num_str]
        return list(map(int, plus))