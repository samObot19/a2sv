class Solution:
    def totalMoney(self, n: int) -> int:
        totalMoney = 0
        
        if n < 7:
            return n*(n + 1)//2
        num = n//7
        
        modulo = n % 7
        a = 1
        b = 7
        for i in range(num):
            totalMoney += (b - a + 1)*(a + b)//2
            a += 1
            b += 1
        
        if modulo != 0:
            print(modulo)
            totalMoney += modulo*(modulo - 1 + 2*a)//2
        return totalMoney