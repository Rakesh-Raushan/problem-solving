# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy_node = ListNode() #dummy node
        merged_head = dummy_node

        
        while(len(lists)):
            min_i = 0
            min_val = float("inf")
            # find index in lists with min val (min lists[i].val)
            for i in range(len(lists)):
                if lists[i]: #that list has to exist before checking its val
                    if lists[i].val < min_val:
                        min_i = i
                        min_val = lists[i].val
            
            #point merged head to that
            merged_head.next = lists[min_i]
            #update the head of list at that index in lists
            lists[min_i] = lists[min_i].next
            #update the head of our merged list
            merged_head = merged_head.next

            lists = [x for x in lists if x]
        
        return dummy_node.next
                