class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def build(cur: List[str], left: int, right: int):
            if left == 0 and right == 0:          # used all pairs
               ans.append(''.join(cur))
               return
            if left > 0:                          # can still add '('
               cur.append('(')
               build(cur, left - 1, right)
               cur.pop()
            if right > left:                      # can add ')' without breaking balance
               cur.append(')')
               build(cur, left, right - 1)
               cur.pop()

        build([], n, n)
        return ans  