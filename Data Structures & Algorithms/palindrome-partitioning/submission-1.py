class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr_part_subs = []
        
        def helper(curr_index):
            if curr_index == len(s):
                result.append(curr_part_subs[:]) #append a copy
            #partition for every index
            for end in range(curr_index, len(s)):
                #check if left sub as per the indices is palindrome
                if self.ispali(s, curr_index, end):
                    #add it to curr part subs
                    curr_part_subs.append(s[curr_index: end+1][:]) #again a copy
                    #recurse on the right sub
                    helper(end+1)
                    #to backtrack remove the appended sub
                    curr_part_subs.pop()
        helper(0)
        return result
        
    def ispali(self, sub, i, j):
        while i < j:
            if sub[i] != sub[j]:
                return False
            i , j = i+1, j-1
        return True

#verify "aab" -> [] "a" is pali so ["a"]; "a" is pali so ["a", "a"]; "b" is pali so ["a", "a", "b"]; BASE so add to result
#BACK and pop ["a", "ab"] not pali so BACK and pop
# [], "aa" is pali so ["aa"], "b" is palli so ["aa", "b"], BASE so add to result
#BACK [] "aab" is not pali
#BACK
#result = [["a", "a", "b"], ["aa", "b"]]



        