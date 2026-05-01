# # class Solution:
# #     def lengthOfLongestSubstring(self, s: str) -> int:
#         # # i am thinking, take a window and maintain a set
#         # # moment you meet a duplicate shrink the window from left and update the set
#         # if len(s)==0:
#         #     return 0
#         # window = set()
#         # L=0
#         # lmax = float("-inf")

#         # for R in range(len(s)):
#         #     while s[R] in window:
#         #         window.remove(s[L])
#         #         L+=1
#         #     window.add(s[R])
#         #     lmax = max(lmax, R-L+1)

#         # return lmax  

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s)==0:
#             return 0
#         i, j =0, 0
#         seen = set()
#         seen.add(s[0])
#         max_len = 1
#         while(j+1 < len(s)):
#             if s[j+1] not in seen:
#                 j+=1
#                 seen.add(s[j])
#                 curr_len = j-i+1
#                 max_len = max(max_len, curr_len)
#             else:
#                 seen.remove(s[j+1])
#                 i+=1
#                 j+=1
#             print(seen)

#         return max_len


# #verification
# # i, j, j+1, s[j+1], seen, curr_len, max_len
# # 0,0,   1,     x ,   {z} ,     2,       2
# # 0, 1,  2,     y ,   {z, x,y},   3,       3
# #        3,     z     
# # 1,     3,     z,    {x,y},     

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        max_len = 0

        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                curr_len = r-l
                max_len = max(curr_len, max_len)
            else:
                seen.remove(s[l])
                l+=1
        
        return max_len

#pwwkew, len=6
# l,r,seen,maxl
# 0,0,{p},1
# 0, 1,{p,w},2
# 1,2, {p}, 2




