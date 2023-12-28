class OrderedStream:
    
    def __init__(self, n: int):
        self.lst = [0 for i in range(1000)]
        self.i = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.lst[idKey - 1] = value
        

        while self.lst[self.i] != 0:
            ans.append(self.lst[self.i])
            self.i += 1
            
        return ans
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)