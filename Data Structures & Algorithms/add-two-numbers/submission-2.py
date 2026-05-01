# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # i =0
        # curr1, curr2 = l1, l2
        # sum1, sum2 = 0, 0
        # while(curr1):
        #     sum1+= curr1.val*(10**i)
        #     i+=1
        #     curr1=curr1.next
        # i=0
        # while(curr2):
        #     sum2+= curr2.val*(10**i)
        #     i+=1
        #     curr2=curr2.next
        
        # sum_total = sum1+sum2
        # if sum_total ==0:
        #     return ListNode()
        # dummy_node = ListNode()
        # curr = dummy_node
        # while(sum_total):
        #     curr.next = ListNode(sum_total%10)
        #     curr = curr.next
        #     sum_total = sum_total//10
        
        # return dummy_node.next

        #a better approach using carry that does not require adding up all the ints which could lead to big numbers

        dummy_node = ListNode()
        curr = dummy_node
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total//10
            curr.next = ListNode(val = total%10)

            #update the pointers for next iter
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy_node.next

        