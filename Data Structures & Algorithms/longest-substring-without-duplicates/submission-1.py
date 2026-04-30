class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        i=j=0
        l=0
        while j<len(s):
            if s[j] not in seen:
                seen.add(s[j])
                l=max(l,j-i+1)
                j+=1
            else:
                i+=1
                j=i
                seen.clear()
                
        return l