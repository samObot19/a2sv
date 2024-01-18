class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 1, len(skill) - 2
        chem = skill[0] + skill[-1]
        total = skill[0]*skill[-1]

        while left < right:
            if skill[left] + skill[right] != chem:
                return -1
            total += skill[left]*skill[right]
            left += 1
            right -= 1
            
        return total