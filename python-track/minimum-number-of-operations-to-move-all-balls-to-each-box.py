class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lst = []
        res = []
        #indexing all ones bit from the string
        for i in range(len(boxes)):
            if boxes[i] == '1':
                lst.append(i)
                
        #iterating the distance of all ones from any  index
                
        for i in range(len(boxes)):
            operations = 0
            for ones in lst:
                operations += abs(ones - i)
                
            res.append(operations)
            
        return res
                
            