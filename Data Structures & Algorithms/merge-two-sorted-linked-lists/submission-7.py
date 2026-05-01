# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode()

        head1 = list1
        head2 = list2
        head = dummyhead

        while head1 and head2:
            if head1.val <= head2.val:
                # head1 is smaller one and should be made next
                head.next = head1
                #update head1
                head1 = head1.next
            else:
                # head2 is smaller and should be made next
                head.next = head2
                #update head2
                head2 = head2.next
            #update head
            head = head.next
        
        #if any of two is left that should be made the next
        head.next = head1 if head1 else head2

        return dummyhead.next
        