class Solution:

    def encode(self, strs: List[str]) -> str:
        #i am thinking i'll use a special character to separate the but since the special char can
        #appear in the strings as well, i'll also encode the len of strings in the string
        #["hello", "world"] to "5#hello5#world"
        # Core idea: if we just use special char, it might be in string and we would break string even where not needed
        #            if we just use len of strings before them, for longer strings say of 23 char, while decoding we would
        #            not know if len is 2 and 3 is part of string or 23 is the len so till we meet #we consider ints to be len
        
        if len(strs)==0:
            return ""
        encoded_string_list = []
        for string in strs:
            if len(string):
                encoded_string_list.extend([str(len(string)), "#", string])
            else:
                encoded_string_list.extend([str(len(string)), "#"])
        return "".join(encoded_string_list)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded_strings = []
        i=0
        while(i<len(s)):
            j=i
            while s[j]!="#":
                j+=1
            len_str = int(s[i:j])
            if not len_str:
                decoded_strings.append("")
                i=j+1
            else:
                i=j+1
                string = s[i:i+len_str]
                decoded_strings.append(string)
                i=i+len_str
        
        return decoded_strings
