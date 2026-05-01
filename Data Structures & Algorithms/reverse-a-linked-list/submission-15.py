# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# head=[0,1,2,3]
# curr =0, prev = None
# while 0 -> temp = 1, 0->None, prev = 0, curr = 1
# while 1 -> temp = 2, 1->0->None, prev = 1, curr = 2
# while 2 -> temp = 3, 2->1->0->None, prev = 2, curr = 3
# while 3 -> temp = None, 3->2->1->0->None, prev = 3, curr = None
# while breaks, return None

# 2->5->7
# head 2, curr 2, prev = None
# till curr.next
#   temp = curr.next (5)
#   curr.next = prev (None)
#   prev = curr (2)
#   curr = temp (5)
# so state here: <-2 (prev) and (curr) 5->7
# next iter:
#   temp = 7
#   curr.next = prev (2); <-2<-5
#   prev = 5
#   curr = 7; 7
# next iter: