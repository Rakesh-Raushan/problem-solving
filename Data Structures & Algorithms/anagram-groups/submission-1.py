class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count_char_map = {}

        for string in strs:
            char_count_str = [0]*26
            for char in string:
                char_idx = ord(char) - ord('a')
                char_count_str[char_idx]+=1
            char_count_str = str(char_count_str)

            if char_count_str in count_char_map:
                count_char_map[char_count_str].append(string)
            else:
                count_char_map[char_count_str] = [string]
        
        return count_char_map.values()

        