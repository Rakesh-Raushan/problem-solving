# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummyhead = ListNode()
        # head1, head2 = list1, list2
        # head = dummyhead

        # while(head1 and head2):
        #     if head1.val <= head2.val:
        #         head.next = head1
        #         head1 = head1.next
        #     else:
        #         head.next = head2
        #         head2 = head2.next
        #     head = head.next
        
        # head.next = head1 if head1 else head2

        # return dummyhead.next

        #recursive
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        