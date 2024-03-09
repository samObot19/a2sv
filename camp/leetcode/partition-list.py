# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        dummy1 = ListNode()
        dummy2 = ListNode()
        high = dummy1
        less = dummy2

        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                high.next = current
                high = high.next

            current = current.next
        less.next = dummy1.next
        high.next = None

        return dummy2.next



        




        