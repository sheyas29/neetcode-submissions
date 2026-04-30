class Solution:
    def isValid(self, s: str) -> bool:
        mapping={')':'(', '}':'{', ']':'['}
        stack=[]

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack:
                    return False
                elif stack.pop()!=mapping[char]:
                    return False
        return not stack