class Solution:
    def freqAlphabets(self, s: str) -> str:
        alph1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        alpha2 = ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        patern = ['10#', '11#' , '12#', '13#', '14#', '15#', '16#', '17#', '18#', '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#']
        
        code = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        dictionary = dict(zip(code, alph1))
        new_dict = dict(zip(patern, alpha2))
        dictionary.update(new_dict)
        i = 0
        decoded = ""
        while i < (len(s)):
            if s[i] == '#':
                i += 1
                continue
                
            if (i < len(s) - 2) and (s[i + 2] == '#'):
                decoded += dictionary[s[i: i + 3]]
                i += 1
            else:
                decoded += dictionary[s[i]]
            i = i + 1
        
        
        return decoded
        
        