class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        ptr1 = len(s) - 1
        ptr2 = 0
        
        while ptr1 >= ptr2:
            temp = s[ptr2]
            s[ptr2] = s[ptr1]
            s[ptr1] = temp
            ptr1 = ptr1 - 1
            ptr2 = ptr2 + 1
        