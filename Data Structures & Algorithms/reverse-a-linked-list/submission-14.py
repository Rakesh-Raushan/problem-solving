# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursive approach
        #BASE case, no head or head.next, i.e case of zero or 1 node, reversed it just head itself
        if not head or not head.next:
            return head

        #recurse on the next nodes
        newhead = self.reverseList(head.next)

        #while backtracking update the links
        head.next.next = head

        #make sure the last head next points to None
        head.next = None

        #return newhead
        return newhead
        