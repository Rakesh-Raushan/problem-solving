# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # again idea would be to use a slow and a fast pointer
        # if cycle exists, fast would meet the slow else never

        #1 node can never have cycle
        if not head.next:
            return False

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        
        return False

        
        