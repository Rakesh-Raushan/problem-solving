# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

#         dummy_head = ListNode()
#         new_curr = dummy_head
#         while True:
#             min_val = float("inf")
#             min_idx = -1
#             for i in range(len(lists)):
#                 if lists[i] and lists[i].val < min_val:
#                     min_val = lists[i].val
#                     min_idx = i
#             #if after all this we see min_idx =-1, means all lists exhausted
#             if min_idx == -1:
#                 break
#             #otherwise we got some min
#             new_curr.next = lists[min_idx]
#             new_curr = new_curr.next

#             #move the pointer of the ll whose min was selected to ahead by 1 pos
#             lists[min_idx] = lists[min_idx].next
        
#         return dummy_head.next

        #above solution is O(nk) solution where n is sum of nodes of k LL and k is total number of LL, since for every node of merged list
        #we are scanning all k lists
        #it can be slow
        #better solution, we can use min heap

class ComparableNodes:
    def __init__(self, node):
        self.node = node
    def __lt__(self,other):
        return self.node.val < other.node.val
        #must implement lt not le, strict comparision happend in heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #put all the nodes to a heap in n operations
        #we will maintain heap of (node.val, node)
        min_heap_nodes = []
        for i in range(len(lists)):
            head_i = lists[i]
            while(head_i):
                heapq.heappush(min_heap_nodes, ComparableNodes(head_i)) #since we wrapped it, the nodes can be directly compared and wont through comparision error
                head_i = head_i.next
        
        #get the min as merged_head
        dummy_merged_head = ListNode()
        #add the rest by popping till we have the heap
        curr = dummy_merged_head
        while min_heap_nodes:
            curr.next = heapq.heappop(min_heap_nodes).node #from the comparable node take out the node
            curr = curr.next
        
        curr.next = None
        
        return dummy_merged_head.next
        





