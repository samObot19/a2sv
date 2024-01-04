class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False #the array must greter than 2
        decr, i = 0, 0
        #ptr for increament and decrement
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1
        # all the array elemnts strictly increasing return false 
        if i + 1 == len(arr) or i == 0:
            return False
        decr = i
        # for decresing sequence of the array
        while decr < len(arr) - 1  and arr[decr] > arr[decr + 1]:
            decr += 1
        #if the sum of increasing and decreasing sequense of the array equal to the length of the array returning true     
        return decr + 1 == len(arr)
        