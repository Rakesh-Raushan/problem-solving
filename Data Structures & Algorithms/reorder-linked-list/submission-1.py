# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #idea is to see it as two halfs and then second half reversed and clubbed alternately with first
        #ex: head = [2,4,6,8] , two halves = [2,4] [6,8], reverse 2nd half so you have [2,4] and [8,6]
        #now start at first and chose alternating between two ll ,you get [2,8,4,6]

        #handle upto 2 size
        # if not head or not head.next or not head.next.next:
        #     return head

        #forming the two half linked lists
        #getting the middle, use slow fast pointer
        s, f = head, head

        while(f and f.next and f.next.next):
            s = s.next
            f = f.next.next

        # slow gives end of first half
        head1 = head
        head2 = s.next

        #make the first half tail none
        s.next = None

        # we need to reverse the ll head2
        prev, curr = None, head2

        while(curr):
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        head2 = prev #the reversed head

        #now we alternate starting from head1 and form the reordered ll
        curr1 = head1
        curr2 = head2
        while curr1 and curr2:
            temp1 = curr1.next
            curr1.next = curr2
            temp2 = curr2.next
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2
        
        head = head1




        

        