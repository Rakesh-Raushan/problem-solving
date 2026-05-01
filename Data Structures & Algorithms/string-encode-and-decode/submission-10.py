class Solution:

    def encode(self, strs: List[str]) -> str:
        #i'll do length(str)+some_special_char+act_str
        encoded_str = ""
        for string in strs:
            str_len = str(len(string))
            encoded_str+=str_len + "#" + string
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        start,end = 0, 0

        while end < len(s):
            while s[end] != "#":
                end+=1
            len_str = int(s[start:end])
            start = end+1
            end = start + len_str
            string = s[start:end][:]
            result.append(string)
            start = end
        
        return result

