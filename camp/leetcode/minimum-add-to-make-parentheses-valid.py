class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openPar, closePar = 0, 0
        #implies open and close parentesis 
        for i in s:
            if i == '(':
                openPar += 1
            elif i == ')'  and openPar > 0: #if there is => '(' before the the current =>')' decrease openPar b/c its already closed
                openPar -= 1
            else: #---------------------may the string element starting from ')' or the other ( are already fulfiled in this case we need another '(' to fullfil this gap 

                closePar  += 1
        #time o(n) 
        #space O(1)
        return openPar + closePar



        