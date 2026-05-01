# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #one node case
        if not head.next:
            return None #given n <=sz
        
        #for any more nodes, we will take 2 pointer approach
        #but if n ==sz even in such cases it can be an issue
        p1 = p2 = head
        for i in range(n):
            p2=p2.next

        if not p2:
            #case: n == sz
            head = head.next
            return head
        
        while(p2.next):
            p1=p1.next
            p2=p2.next
        
        p1.next = p1.next.next
        return head

        