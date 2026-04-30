class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    # mapping stores *functions*, not pre-computed numbers
        mapping = {
                   '+': lambda b, a: a + b,
                   '-': lambda b, a: b - a,
                   '*': lambda b, a: a * b,
                   '/': lambda b, a: int(b / a)   # truncate toward zero
                  }
        for char in tokens:
            if char not in mapping:
                stack.append(int(char))    # store as int
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(mapping[char](b, a))  # apply operator
        return stack[0]