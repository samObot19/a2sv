# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastPtr = head
        slowPtr = head

        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next

        return slowPtr
        