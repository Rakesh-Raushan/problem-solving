class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True 

    def search(self, word: str) -> bool:
        def rec_search(word,index, root):
            #base case:
            if index == len(word):
                return root.word
            
            c = word[index]
            if c ==".":
                for child in root.children:
                    if rec_search(word, index+1, root.children[child]):
                        return True
            elif c in root.children:
                return rec_search(word, index+1, root.children[c])

            return False


        return rec_search(word,0, self.root)
        
