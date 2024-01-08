class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashMap = defaultdict(lambda: [])
        diagonal = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                hashMap[i + j].append(mat[i][j])
        
        lst = list(hashMap.values())
        for i in range(len(lst)):
            if i % 2 == 0:
                lst[i].reverse()

        for i in lst:
            for j in i:
                diagonal.append(j)
        

        return diagonal