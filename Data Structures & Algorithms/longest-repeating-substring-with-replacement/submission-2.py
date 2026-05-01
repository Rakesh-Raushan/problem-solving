class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #uppercase, atmost k replacement
        #left pointer and right pointer both at 0 initially,
        # maintain a char_count so that we can check as we move right pointer, that
        # we have window length - most freq char count < k, if not so move left till it happens
        # moving left would, remove from char_count and increase l

        left = 0
        char_count = {}
        max_len = float("-inf")

        for right in range(len(s)):
            #add char to window defined by (l,r+1)
            char_count[s[right]] = 1 + char_count.get(s[right], 0)

            #check if its a valid window
            #windowlen - mostfreq < k, if needed make it valid
            while(right+1-left - max(char_count.values()) > k):
                char_count[s[left]] = char_count.get(s[left]) - 1
                left+=1
            
            max_len = max(max_len, right+1-left)
        
        return max_len