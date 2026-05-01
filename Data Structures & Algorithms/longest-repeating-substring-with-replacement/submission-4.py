class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maintain two pointers left and right to mark the curr window of chars
        # make sure the window is valid in terms of max k replacement 
        # the window len - count of most freq char should be less than k allowed

        left = 0
        count_char = {}
        max_len = 0

        for right in range(len(s)):
            #update the count_char to include this char
            count_char[s[right]] = 1 + count_char.get(s[right], 0)

            #if including this char made the window invalid shrink the window
            while(right+1 - left - max(count_char.values()) > k):
                count_char[s[left]] = count_char.get(s[left]) - 1
                left+=1
            
            #check if this valid window is bigger than max then update max
            max_len = max(max_len, right+1-left)
        
        return max_len
        