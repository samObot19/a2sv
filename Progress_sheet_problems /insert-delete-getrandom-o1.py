class RandomizedSet:

    def __init__(self):
        self.sets = defaultdict(lambda:0)

    def insert(self, val: int) -> bool:
        if self.sets[val] == 0:
            self.sets[val] += 1
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if self.sets[val] > 0:
            self.sets[val] -= 1
            return True
        return False
        
        
    def getRandom(self) -> int:
        return random.choices([i for i in self.sets.keys() if self.sets[i] > 0])[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()