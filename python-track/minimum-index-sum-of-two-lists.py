class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lst = []
        dic = defaultdict(lambda : [])
        for i in range(len(list1)):
            for j in range(len(list2)):
                if (list1[i] == list2[j]):
                        dic[i + j].append(list1[i])
                        lst.append(i + j)
                    
        
        
        return dic[min(lst)]
        
    
        
        