class Solution:
    def fib(self, n: int) -> int:
        def Fibonacci(k):
            if k <= 1:
                return k  
            else:
                return Fibonacci(k - 1) + Fibonacci(k - 2)
        return Fibonacci(n)