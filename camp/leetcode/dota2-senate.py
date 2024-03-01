class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()
        n = len(senate)

        for index, s in enumerate(senate):
            if s == 'R':
                R.append(index)
            else:
                D.append(index)
        
        while R and D:
            if R[0] < D[0]:
                R.append(n)
            else:
                D.append(n)
            n += 1
            R.popleft()
            D.popleft()

        if D: return "Dire"
        if R: return "Radiant"
            
        