class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':          # empty cell, skip
                   continue
                b = (r // 3) * 3 + (c // 3)

            # check all three sticker pages
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                   return False        # page ripped!

            # stick the digit
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        return True   # no rips anywhere