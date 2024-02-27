class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:  #the base case 
            return 1
        if n < 0: #handling the negative exponent
            return 1/self.myPow(x, abs(n))        
        if n % 2 == 0:#divide the problem into more simpler one as long as its goes to the easiest one
            return self.myPow(x*x, n//2)  
        else:
            return x*self.myPow(x*x, (n - 1)//2)

        