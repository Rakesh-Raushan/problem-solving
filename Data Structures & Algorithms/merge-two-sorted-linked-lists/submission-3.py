# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyhead = ListNode()
        head1, head2 = list1, list2
        head = dummyhead

        while(head1 and head2):
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        
        head.next = head1 if head1 else head2

        newhead = dummyhead.next
        del dummyhead
        return newhead
        