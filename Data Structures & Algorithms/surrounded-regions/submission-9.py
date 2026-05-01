class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #another iterative approach
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        queue = deque()

        # Step 1: Add all boundary 'O's to the queue
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    queue.append((r, c))
        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == 'O':
                    queue.append((r, c))
        
        # Step 2: BFS from boundary 'O's and mark as 'T'
        while queue:
            r, c = queue.popleft()
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    queue.append((r + dr, c + dc))
        
        # Step 3: Flip the surrounded 'O's to 'X', and 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        