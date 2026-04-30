class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for char in operations:
            try:
                # This handles both "5" and "-5"
                num = int(char)
                stack.append(num)
                res += num
            except ValueError:
                # If it's not a number, check the other operations
                if char == "+":
                    # Note: Peek at the last two, don't remove them yet
                    a = stack[-1]
                    b = stack[-2]
                    ans = a + b
                    stack.append(ans)
                    res += ans
                elif char == "C":
                    remove = stack.pop()
                    res -= remove
                elif char == "D":
                    double = 2 * stack[-1]
                    stack.append(double)
                    res += double
                    
        return res
            