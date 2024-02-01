# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next: #get the middle
            slow = slow.next
            fast = fast.next.next

        curr, prev, it  = slow, None, head

        while curr: # reverse after middle
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward

        while prev: #cheacking the reversed after middle element and from starting ptr of the list
            if prev.val != it.val:
                return False
            prev = prev.next
            it = it.next
            
            
        return True
        