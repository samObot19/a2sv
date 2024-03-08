class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = []
        self.times = []
        self.dic = collections.defaultdict(int)
        self.c = 0

        for i in range(len(times)):
            self.times.append(times[i])
            self.dic[persons[i]] += 1
            if self.dic[persons[i]] >= self.c:
                self.persons.append(persons[i])
                self.c = self.dic[persons[i]]
            else:
                self.persons.append(self.persons[-1])

    def q(self, t: int) -> int:
        winner = bisect_right(self.times, t)
        return self.persons[winner - 1]




# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)