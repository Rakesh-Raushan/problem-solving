class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Break the list into groups of k
        groups = []
        curr = head
        while curr:
            group_head = curr
            count = 1
            group_curr = group_head
            
            # Find the k-th node or the end of the list
            while count < k and group_curr.next:
                group_curr = group_curr.next
                count += 1
            
            # Save the start of the next group before breaking the connection
            next_group = group_curr.next
            
            # Break the connection for this group
            group_curr.next = None
            
            # Add the group to our list
            groups.append((group_head, count))  # Store the group head and its size
            
            # Move to the next group
            curr = next_group
        
        # Step 2: Reverse each complete group (of size k)
        def reverse_list(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        # Apply reverse_list to each complete group
        reversed_groups = []
        for group_head, count in groups:
            if count == k:  # Only reverse if we have exactly k nodes
                reversed_groups.append(reverse_list(group_head))
            else:
                reversed_groups.append(group_head)  # Keep as is if incomplete
        
        # Step 3: Join the groups back together
        dummy_head = ListNode(0)
        curr_tail = dummy_head
        
        for group in reversed_groups:
            curr_tail.next = group
            
            # Find the end of this group
            curr = group
            while curr and curr.next:
                curr = curr.next
            
            # Update the tail pointer
            curr_tail = curr
        
        # Step 4: Return the merged list (after dummy head)
        return dummy_head.next