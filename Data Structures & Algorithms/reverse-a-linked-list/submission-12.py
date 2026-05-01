# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, curr = None, head

        while curr and curr.next:
            print(curr.val, curr.next.val)
            #hold curr.next before reversing its link
            temp = curr.next
            #reverse its link
            curr.next = prev

            #update pointers
            prev = curr
            curr = temp
        
        curr.next = prev
        return curr
        

#0,1,2,3
#0->1->2->3->
#prev = None, cur=0, curr.next 1 exists so , <-0 1->2->3->
#prev=0, cur=1 curr.next= 2 exists so: <-0<-1 2->3->
#prev=1, cur=2,curr.next= 3 exists so: <-0<-1<-2 3->
#prev=2, cur=3,curr.next= None, does not exist break loop
        