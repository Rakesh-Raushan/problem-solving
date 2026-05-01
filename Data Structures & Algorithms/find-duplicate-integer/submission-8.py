class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #if we consider the list as linkedlist with following link rule
        #every val is linked to number at idx=val e.g
        # [1,2,3,2,2]; 1 ->val ati=1i.e2 ,  2->val at i=2i.e3, 3->val at i=3i.e2; 
        #we see we arrive a cycle when we meet a duplicate so a simple cycle detection can be done here
        # we can use slow and fast pointer for the same; further the start of cycle will give us the duplicate num

        #so we imagine [1,2,3,2,2] as 1 -> 2 ->3->2

        slow = fast = nums[0]
        while True:
            slow = nums[slow] #speed one
            fast = nums[nums[fast]] #speed two

            if slow ==fast:
                #cycle detected or duplicate, so break
                break
        
        #use another slow to detect the start of cycle or the duplicate num
        slow2 = nums[0]

        while True:
            if slow == slow2:
                return slow
            slow2 = nums[slow2]
            slow = nums[slow]
        
        #verify [1,2,3,2,2]; s,f = 1, curr = 1
        #s = nums[s]=2,f=nums[nums[f]]=nums[2]=3; s=2, f=3 not same
        #s=nums[s]=nums[2]=3, f=nums[nums[f]]=nums[nums[3]]=nums[2]=3; s==f; so break
        #s1=1,curr=1,s1=nums[1]=2,s2=nums[3]=2, s1==s2; return s1=2 works
        #verify [1,2,3,4,4]
        #s=1,f=1,s=2,f=3,s=3,f=4,s=4,4 break
        #s2=1,s=4,s
        #[3,1,3,4,2]
        #s=3,f=3,s=4,f=2,s=2,f4,s=3,f=3 break
        #s2=3,s=3,s2=4,


            

        