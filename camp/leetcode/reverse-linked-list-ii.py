# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        current = head

        while current:
            lst.append(current.val)
            current = current.next

        while left < right:
            lst[left - 1], lst[right - 1] = lst[right - 1], lst[left - 1]
            right -= 1
            left += 1

        Node = head
        i = 0

        while Node:
            Node.val = lst[i]
            Node = Node.next
            i += 1

        return head

        