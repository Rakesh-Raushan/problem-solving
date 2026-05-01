# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # let's take two pointers marking the prev and cur
        # prev, cur = None, head
        # while(cur):
        #     temp = cur.next
        #     cur.next = prev
        #     # update the pointers
        #     prev = cur
        #     cur = temp
        
        # return prev
        # do it with recursion
        # zero nodes case
        if not head:
            return None
        # one node case
        new_head = head

        # if more nodes, new_head has to be found by going to depth
        if head.next:
            #recurse on them for new_head
            new_head = self.reverseList(head.next)
            #update their next while backtracking
            head.next.next = head
        #final node should point to none
        head.next = None
        # return new head
        return new_head
        