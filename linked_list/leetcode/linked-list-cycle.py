# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tor = rab = head

        while rab and rab.next:
            rab = rab.next.next
            tor = tor.next

            if rab == tor:
                break
        else:
            return False

        return True
        