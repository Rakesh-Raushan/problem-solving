# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative solution: more intuitive

        # #two pointer approach
        # prev, curr = None, head

        # while(curr):
        #     #hold nex
        #     temp = curr.next
        #     #update link
        #     curr.next = prev

        #     #prepare for next iter
        #     prev = curr
        #     curr = temp
        
        # #at this point prev is the head of reveresed list
        # return prev

        #recursive solution

        #base case: zero or one node needs no reversal 
        if not head or not head.next:
            return head
        #for longer ones, recurse them till last and last node returned will be the newhead
        newhead = self.reverseList(head.next)
        #as we backtrack, we reverse the link to oppo dir and also remove the original fwd link
        head.next.next, head.next = head, None

        return newhead

        


        