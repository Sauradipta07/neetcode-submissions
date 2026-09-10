"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        map={}
        while curr:
            new=Node(curr.val)
            map[curr]=new
            curr=curr.next
        curr=head
        while curr:
            map[curr].next=map.get(curr.next)
            map[curr].random=map.get(curr.random)
            curr=curr.next
        return map[head]

        