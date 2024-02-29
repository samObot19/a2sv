# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy_head = ListNode()
        prev, cur = dummy_head, head

        while cur:
            nxt = cur.next

            while prev.next is not None and prev.next.val < cur.val:
                prev = prev.next

            prev.next, cur.next = cur, prev.next
            prev = dummy_head

            cur = nxt

        return dummy_head.next