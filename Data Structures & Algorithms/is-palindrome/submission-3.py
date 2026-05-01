class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we can compare left and right to ensure they are same char or not
        # ignore all non-alphanumerice
        # s = "".join([x.lower() for x in s if x.isalnum()]), we can do this but this would take extra space
        # let's check in place
        l, r = 0, len(s)-1
        while(l<r):
            if s[l].isalnum() and s[r].isalnum() and s[l].lower() != s[r].lower():
                return False
            elif not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                l+=1
                r-=1
        return True
        