# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # a1->b1->c1 , a2->b2->c2 ; three pointers
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        cur1 = list1
        cur2 = list2
        if cur1.val < cur2.val:
            cur3 = ListNode(val = cur1.val)
            cur1 = cur1.next
        else:
            cur3 = ListNode(val = cur2.val)
            cur2 = cur2.next
        new_head = cur3

        while(cur1 and cur2):
            cur3.next = ListNode()
            cur3 = cur3.next
            if cur1.val < cur2.val:
                cur3.val = cur1.val
                cur1 = cur1.next
            elif cur1.val > cur2.val:
                cur3.val = cur2.val
                cur2 = cur2.next
            else:
                cur3.val = cur1.val
                cur3.next = ListNode()
                cur3 = cur3.next
                cur3.val = cur2.val
                cur1 = cur1.next
                cur2 = cur2.next
        while(cur1):
            cur3.next = ListNode()
            cur3 = cur3.next
            cur3.val = cur1.val
            cur1 = cur1.next
        while(cur2):
            cur3.next = ListNode()
            cur3 = cur3.next
            cur3.val = cur2.val
            cur2 = cur2.next
        return new_head

        