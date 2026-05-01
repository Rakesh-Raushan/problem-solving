# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #let's use recursion to continuously break links and update them to point them to prev but before that hold them in temp
        #       A - > B -> C -> None
        #prev   curr
        #     <-A     B
        #       prev  curr
        #     <-A <-  B    c
        #             prev  curr
        #     <-A <-  B    c
        # prev = None
        # curr = head
        # if not curr:
        #     return curr

        # while(curr and curr.next):
        #     temp = curr.next
        #     curr.next = prev

        #     #update for next
        #     prev = curr
        #     curr = temp
        # curr.next = prev

        # return curr

        #above iterative solution works but let's also write recursive
        #base case when we are at end
        #zero nodes case
        if not head:
            return None
        #one node case
        newhead = head

        #for any more nodes, call recursively
        if head.next:
            newhead = self.reverseList(head.next)
            #while backtracking update directions
            head.next.next = head

        #before returning, make sure last node points to None in the reversed list
        head.next = None

        return newhead


        


        