class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        TOTAL_CELLS = ROWS * COLS
        
        if len(word) > TOTAL_CELLS:
            return False

        # --- Micro-Optimization 1: Flatten the board to 1D ---
        # This reduces 2D array overhead down to a single 1D index lookup
        flat_board = []
        for row in board:
            flat_board.extend(row)

        # --- Micro-Optimization 2: Low-overhead Frequency Check ---
        # Using a fast list/dict allocation instead of Counter()
        board_counts = {}
        for char in flat_board:
            board_counts[char] = board_counts.get(char, 0) + 1

        word_counts = {}
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1

        for char, count in word_counts.items():
            if board_counts.get(char, 0) < count:
                return False

        # Reversal trick based on character frequency
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        # Convert word to ascii values or just keep it as characters
        word_len = len(word)
        target_first = word[0]

        # --- Micro-Optimization 3: Highly streamlined 1D DFS ---
        def dfs(pos, index):
            if index == word_len:
                return True
            
            if flat_board[pos] != word[index]:
                return False
            
            # If we reached the last character match successfully
            if index == word_len - 1:
                return True

            # In-place tracking
            original_char = flat_board[pos]
            flat_board[pos] = '#'

            # 1D Directional moves: Calculate grid neighbors
            r, c = divmod(pos, COLS)
            
            # Check Down
            if r < ROWS - 1 and dfs(pos + COLS, index + 1):
                return True
            # Check Up
            if r > 0 and dfs(pos - COLS, index + 1):
                return True
            # Check Right
            if c < COLS - 1 and dfs(pos + 1, index + 1):
                return True
            # Check Left
            if c > 0 and dfs(pos - 1, index + 1):
                return True

            # Backtrack
            flat_board[pos] = original_char
            return False

        # Start search
        for i in range(TOTAL_CELLS):
            if flat_board[i] == target_first:
                if dfs(i, 0):
                    return True

        return False