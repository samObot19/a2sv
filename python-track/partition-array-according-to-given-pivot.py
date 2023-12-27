class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = [i for i in nums if i < pivot]
        middle = [i for i in nums if i == pivot]
        right = [i for i in nums if i > pivot]
        
        left.extend(middle)
        left.extend(right)
            
        
        
        return left
                