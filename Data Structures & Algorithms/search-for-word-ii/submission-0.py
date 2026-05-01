class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Build a trie of the words given to efficiently search prefixes
        # This allows us to quickly determine if a path could lead to a valid word
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isword = False
        
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def add_word(self, word):
                cur = self.root
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.isword = True
        
        # Add all words to the trie
        words_trie = Trie()
        for w in words:
            words_trie.add_word(w)
        
        # Global result set to store found words
        result = set()
        rows, cols = len(board), len(board[0])
        
        # DFS to explore all possible paths from each cell in the board
        # We pass:
        # - r, c: current position in the board
        # - root: current node in the trie
        # - word: current word being formed
        # - visited: set of already visited positions to avoid reusing cells
        def dfs(r, c, root, word, visited):
            # Base cases to terminate exploration:
            # 1. Out of board boundaries
            # 2. Cell already visited
            # 3. Current character doesn't exist in the trie node's children
            if (r < 0 or c < 0 or r == rows or c == cols or
                (r, c) in visited or board[r][c] not in root.children):
                return
            
            # Mark current cell as visited
            visited.add((r, c))
            
            # Move to the next node in trie and add character to current word
            root = root.children[board[r][c]]
            word += board[r][c]
            
            # If we've found a complete word, add it to results
            if root.isword:
                result.add(word)
            
            # Explore all four directions (up, down, left, right)
            dfs(r+1, c, root, word, visited)  # down
            dfs(r-1, c, root, word, visited)  # up
            dfs(r, c+1, root, word, visited)  # right
            dfs(r, c-1, root, word, visited)  # left
            
            # Backtrack: remove the cell from visited set when we're done exploring
            # This is crucial to allow this cell to be used in other paths
            visited.remove((r, c))
        
        # Start DFS from each cell in the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, words_trie.root, "", set())
        
        return list(result)