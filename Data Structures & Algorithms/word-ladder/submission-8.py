class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #I am thinking if we can design it as a graph
        #adj list of words and to words where we can next move from it
        #i can make a func to check if it can be valid next or not
        #once i have the adj list, i can do a BFS from begin word and try to reach wordlist
        #BFS will give me the shortest path

        def valid_next(word, next_word):
            #given all words of same length and lowercase and distinct
            diff = 0
            for i in range(len(word)):
                if word[i]!= next_word[i]:
                    diff+=1
            return diff==1


        #create adj
        wordList.append(beginWord)
        # wordList.append(endWord)
        word_set = set(wordList)
        all_words = list(word_set)
        adj = {}
        for word in all_words:
            adj[word] = [x for x in all_words if valid_next(word, x)]

        # adj= {cat: [bat, sat], bat: [cat, bag, sat], bag: [bat,dag], sat: [cat,bat], dag:[bag], dot:[]}
        
        #we have adj and we need to bfs it to get shortest way to reach
        from collections import deque
        queue = deque([beginWord])
        visited = set([beginWord])

        transforms_needed = 1
        while queue:
            for _ in range(len(queue)):
                w = queue.popleft()
                if w == endWord:
                    return transforms_needed

                for next_w in adj[w]:
                    if next_w not in visited:
                        visited.add(next_w)
                        queue.append(next_w)
            transforms_needed+=1
        
        return 0
        #cat q=[bat,sat], bat, q=[sat,bag], sat, q=[bag], bag, q=[dag], dag, q=[]

        

        