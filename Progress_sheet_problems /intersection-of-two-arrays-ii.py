class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = Counter(nums1) #the occurence of elements in nums1
        ans = [] 
        for i in nums2:
            if freq[i] > 0:   #if the frequency greater than 0 the element in nums2 exist in nums1
                ans.append(i)
                freq[i] -= 1  # decreamenting the occurence of the element to avoid duplicate elment
        return ans