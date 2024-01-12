class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged = []

        while(i < len(word1) and j < len(word2)):
            if word1[i] > word2[j]:
                merged.append(word1[i])
                i += 1
            elif word1[i] < word2[j]:
                merged.append(word2[j])
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    merged.append(word1[i])
                    i += 1
                elif word1[i:] <= word2[j:]:
                    merged.append(word2[j])
                    j += 1
                

        merged.extend(list(word1[i:]))
        merged.extend(list(word2[j:]))

        return "".join(merged)
        