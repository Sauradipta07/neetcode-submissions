# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse1grp(self,head,k):
        cur=head
        prev=None
        for i in range(k):
            NextNode=cur.next
            cur.next=prev
            prev=cur
            cur=NextNode
        return prev,head,cur
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k==1:
            return head

        plac=ListNode(0)
        plac.next=head
        prev_grp=plac
        grp_start=head
        while True:
            cur=grp_start
            count=0
            while cur is not None and count < k:
                cur = cur.next
                count += 1
            if count < k:
                break
            new_head, grp_tail, next_grp = self.reverse1grp(grp_start, k)
            prev_grp.next = new_head
            grp_tail.next = next_grp
            prev_grp = grp_tail
            grp_start = next_grp

        return plac.next
        