class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     # first let's brute force it by comparing every string with every other, n(n-1)/2 pairs
    #     res = defaultdict(list)

    #     for s in strs:
    #         sorted_s = "".join(sorted(s))
    #         res[sorted_s].append(s)
        
    #     return list(res.values())

    #idea is to create a hashmap with keys of the sorted strs(sorted anagrams will be same string and hence same key), so just append the strings
    #to the value list of these keys {"sorted_s": ["s1", "s2",...]}
    #e.g strs = ["act","pots","tops","cat","stop","hat"]
    # "act" -> sorted = "act" so entry in hashmap = {"act": ["act"]}; "pots" -> sorted = "opst" so entry {"opst": ["pots"]}
    # "tops" -. sorted = "opst" so goes to same key and entry is updates to {"opts": ["pots", "tops"]} and so on
    # so we traverse the list once, so if n strings we do the exercise n times, and each one involves sorting so if avg str size is m, each takes mlogm
    # so overall time complexity: n*mlogm, space wise, we create n entries in hashmap in worst case where all are different strs so complexity O(n)

    #another better solution would be to do the same thing but without using sorting (to avoid mlogm)
    # we can do this by, using a key of char counts in array of 26 and using that as a string rather than sorted string
    # e.g for "act", key = [1,0,1,0,0,0,0,...,1,0,0,0...], i.e 1 at a c and t positions and string key = "10100...1000...."
    # so enntries will be like {"101000...1000...": ["act"]}
    #code
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count_arr = [0]*26
            for ch in s:
                count_arr[ord(ch) - ord("a")]+=1
            res[tuple(count_arr)].append(s)
        
        return list(res.values())
    #remm if you used count_arr_str  instead of tuple as keys like # count_arr_key = "".join([str(x) for x in count_arr])
    # case like strs=["bdddddddddd","bbbbbbbbbbc"] will fail as 10 and [1,0] will lead to same strings on joining
    #now coming to complexity here, again we traverse all n, and for each n we do m avg string size traversal for count arr so
    # time complexity O(m*n) better than last, space complexity though remains same as we create the same dict so O(n)

    #overall, in this solution remm: we traverse the list to create a hashmap of {"same_keys_for_anagrams" : list(strs)}
    # Traverse each string and build a hashmap:
    # { canonical_key_of_string : [ all strings with that same key ] }
    # where canonical_key can be either:
    #   - ''.join(sorted(s))          (O(m log m) per string)
    #   - tuple(char_counts)          (O(m) per string, for fixed alphabet)
    
    # res = empty hashmap
    # for each word in strs:
    #     key = normalized form that identifies its anagram group
    #     res[key].append(word)
    # return all value-lists in res

