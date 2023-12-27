class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], 
               ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], 
               ['z', 'x', 'c', 'v', 'b', 'n', 'm']
              ]
        def findRow(character):
            if  character in keyboard[0]:
                return 0
            elif character in keyboard[1]:
                return 1
            else:
                return 2
        
        words_in_the_same_row = []
        for word in words:
            letter = word.lower()
            firstCharRow = findRow(letter[0])
            isThere = True
            for character in letter:
                if character in keyboard[firstCharRow]:
                    continue
                else:
                    isThere = False
                    break
            if isThere:
                words_in_the_same_row.append(word)
                
        return words_in_the_same_row
        
        