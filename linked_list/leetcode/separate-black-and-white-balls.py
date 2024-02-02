class Solution:
    def minimumSteps(self, s: str) -> int:
        left_pointer, right_pointer, bill = 0, len(s) - 1, 0

        while left_pointer < right_pointer:

            while left_pointer < len(s) and s[left_pointer] != '1':
                left_pointer += 1

            while right_pointer >= 0 and s[right_pointer] != '0':
                right_pointer -= 1
        
            if left_pointer < right_pointer:
                bill += right_pointer - left_pointer
                left_pointer += 1
                right_pointer -= 1

        return bill