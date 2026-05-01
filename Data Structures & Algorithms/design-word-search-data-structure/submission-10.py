class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True
        

    def search(self, word: str) -> bool:

        def rec_search(i, cur):
            #base case pos
            if i ==len(word):
                return cur.isword
            
            #base case neg
            if word[i] not in cur.children and word[i] != ".":
                return False

            #otherwise for "."
            if word[i] == ".":
                for child in cur.children:
                    if rec_search(i+1, cur.children[child]):
                        return True
            elif word[i] in cur.children: 
                cur = cur.children[word[i]]
                return rec_search(i+1, cur)
            
            return False

        cur = self.root
        return rec_search(0, cur)
    #verify search(".ay"), 
    # i=0, rec_search(0), word[0] = "."
        #cur children d, b, m, s, d
            #cur at d,
                #i = 1, rec_search(1), word[1] = "a"
                #"a" is child of d trienode, cur now at a
                    #rec_search(i=2), word[2] "y", 
                    #"y" is child of d trienode, cur now at "y"
                        #rec_search(i=3) base case so is word true
    #"b.."


        
