class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch for ch in s if ch.isalnum()).lower()
        n=len(s)

        return s[:n//2] == s[-(n//2):][::-1] if n!=1 else True
