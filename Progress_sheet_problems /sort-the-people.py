class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        # for i in range(n):
        #     max = i
        #     for j in range(i, n):
        #         if heights[max] < heights[j]:
        #             max = j
        #     heights[i], heights[max] = heights[max], heights[i]
        #     names[i], names[max] = names[max], names[i]

        # return names

        for i in range(1, n):
            key = heights[i]
            key_name = names[i]
            j = i-1
            while j >= 0 and key > heights[j] :
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            heights[j + 1] = key
            names[j  + 1] = key_name

        return names

 