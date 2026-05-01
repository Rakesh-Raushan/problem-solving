class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # count_char_map = {}

        # for string in strs:
        #     char_count_str = [0]*26
        #     for char in string:
        #         char_idx = ord(char) - ord('a')
        #         char_count_str[char_idx]+=1
        #     char_count_str = str(char_count_str)

        #     if char_count_str in count_char_map:
        #         count_char_map[char_count_str].append(string)
        #     else:
        #         count_char_map[char_count_str] = [string]
        
        # return count_char_map.values()

        seen = dict()

        for string in strs:
            # string_counter = Counter(string)
            # dict can't be hashed as it is mutatble but you can have a tuple of 26 size for alphabets as they are all
            # lowercase alphabets, so
            string_counter = [0]*26
            for char in string:
                string_counter[ord(char) - ord("a")]+=1
            
            string_counter = tuple(string_counter)
            if string_counter in seen:
                seen[string_counter].append(string)
            else:
                seen[string_counter] = [string]
        
        return list(seen.values())

        #["act","pots","tops","cat","stop","hat"]
        #seen = {}
        #act - > str counter = {a:1,c:1,t:1} not in seen so seen = {{a:1,c:1,t:1}: [act]}
        #pots -> str counter = {p:1,o:1,t:1,s:1} not in seen 
        #so seen = {{a:1,c:1,t:1}: [act], {p:1,o:1,t:1,s:1}: [pots]}
        #tops -> str counter = {p:1,o:1,t:1,s:1} in seen so seen = {{a:1,c:1,t:1}: [act], {p:1,o:1,t:1,s:1}: [pots, tops]}
        #cat -> again found in seen so  seen = {{a:1,c:1,t:1}: [act, cat], {p:1,o:1,t:1,s:1}: [pots, tops]}
        #stop -> again found so append so seen = {{a:1,c:1,t:1}: [act, cat], {p:1,o:1,t:1,s:1}: [pots, tops, stop]}
        #hat-> not found 
        #so seen = {{a:1,c:1,t:1}: [act, cat], {p:1,o:1,t:1,s:1}: [pots, tops, stop], {h:1, a:1, t:1} = [hat]}
        #return [[act, cat], [pots, tops, stop], [hat]]

        