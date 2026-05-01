# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        #disconnect first half
        slow.next = None
        #reverse second
        prev, curr = None, second

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        head2 = prev
        head1 = head

        #alternately connect these
        while head1 and head2:
            temp1 = head1.next
            head1.next = head2

            temp2 = head2.next
            head2.next = temp1

            head1 = temp1
            head2 = temp2

        #[2,4,6,8,10] [2,4] [6,8,10] 
        #[2,4] [10,8,6]  2>10
        
        