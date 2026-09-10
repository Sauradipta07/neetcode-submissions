# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=1
        initial=head
        original=head
        while initial.next is not None:
            initial=initial.next
            size+=1
        target=size-n
        if target == 0:
            return original.next
        for i in range(target-1):
            head=head.next
        head.next=head.next.next
        return original

        