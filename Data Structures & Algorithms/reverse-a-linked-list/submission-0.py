# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # let's take two pointers marking the prev and cur
        prev, cur = None, head
        while(cur):
            temp = cur.next
            cur.next = prev
            # update the pointers
            prev = cur
            cur = temp
        
        return prev