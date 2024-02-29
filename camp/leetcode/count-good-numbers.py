class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Mod = 10**9 + 7
        # # if n == 1:  <->the recursive approch
        # #     return 5
        # # if n == 2:
        # #     return 20
        # # if n == 3: 
        # #     return 100

        # # return 20*self.countGoodNumbers(n - 2) % Mod
        
        return (pow(5,(n + 1)//2,Mod)*pow(4,n//2,Mod))%Mod
        


        