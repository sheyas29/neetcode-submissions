class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Split by slashes; filter out empty strings caused by '//'
        parts = path.split("/")
        
        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or not part:
                # Current directory or empty string from extra slashes
                continue
            else:
                # Valid directory or file name (e.g., "...", "home")
                stack.append(part)
                
        return "/" + "/".join(stack)
            