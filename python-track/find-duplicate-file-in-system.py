class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_content = defaultdict(lambda: [])
        ans =[]
        for i in paths:
            content = i.split()
            for i in range(1, len(content)):
                data = content[i].split('(')
                path_content[data[1]].append(content[0] + "/" + data[0])
                
        for i in path_content.values():
            if len(i) >= 2:
                ans.append(i)
        
        return ans        

        
        
            
        
        