# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy_head = ListNode()
        new_curr = dummy_head
        while True:
            min_val = float("inf")
            min_idx = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_idx = i
            #if after all this we see min_idx =-1, means all lists exhausted
            if min_idx == -1:
                break
            #otherwise we got some min
            new_curr.next = lists[min_idx]
            new_curr = new_curr.next

            #move the pointer of the ll whose min was selected to ahead by 1 pos
            lists[min_idx] = lists[min_idx].next
        
        return dummy_head.next




        