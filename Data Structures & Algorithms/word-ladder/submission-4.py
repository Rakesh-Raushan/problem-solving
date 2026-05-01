class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_one_letter_diff(w1,w2):
            return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1

        word_set= set(wordList)
        if endWord not in word_set:
            return 0
        
        from collections import deque

        queue = deque([beginWord])
        n_transform = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return n_transform
                neighbour_words = [x for x in word_set if is_one_letter_diff(x, word)]

                for nw in neighbour_words:
                    queue.append(nw)
                    word_set.remove(nw)
            n_transform+=1
        
        return 0

#Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
#Output: 4
#visited = {}, queue = ["cat"], n_transform = 1
#len queue = 1, word = cat not endword, visited = {"cat"}, nei words = [bat], queue = [bat], n_transform = 2
#len queue = 1, word = bat not endword, visited = {"cat", "bat"}. nei words = [bat, bag], queue = [bag], n_transform = 3
#len queue = 1, word bag not the endword, visited = {"cat", "bat", "bag"}, nei words = [bat,bag,sag,dag], queue = [sag,dag], n_transform = 4
#len queue = 2, word dag not the endword, visited = {"cat", "bat", "bag", "dag"}
        #nei words = [bag,sag,dag]


            
            
            
