# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # we can compare left and right to ensure they are same char or not
#         # ignore all non-alphanumerice
#         # s = "".join([x.lower() for x in s if x.isalnum()]), we can do this but this would take extra space
#         # let's check in place
#         l, r = 0, len(s)-1
#         # while(l<r):
#         #     if s[l].isalnum() and s[r].isalnum():
#         #         if s[l].lower() != s[r].lower():
#         #             return False
#         #         else:
#         #             l+=1
#         #             r-=1
#         #     elif not s[l].isalnum():
#         #         l+=1
#         #     elif not s[r].isalnum():
#         #         r-=1
#         # return True
#         # above if based conditionals skip non alpha numeric one by one, we can further make it explicit to skip them
#         # in one go as well with somethink like below:
#         while(l<r):
#             while l<r and not s[l].isalnum():
#                 l+=1
#             while l<r and not s[r].isalnum(): 
#                 r-=1
#             #skip all the non alphnums from right and left beforehand, then compare
#             if s[l].lower() != s[r].lower():
#                 return False
#             l+=1
#             r-=1
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        left_p, right_p = 0, len(s)-1
        
        while(left_p < right_p):
            while left_p < right_p and not s[left_p].isalnum():
                left_p+=1
            while left_p < right_p and not s[right_p].isalnum():
                right_p-=1
            if s[left_p].lower() != s[right_p].lower():
                return False
            left_p+=1
            right_p-=1
        return True



