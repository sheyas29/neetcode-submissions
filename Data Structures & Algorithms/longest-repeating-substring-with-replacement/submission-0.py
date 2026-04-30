class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        l=0 
        
        d={}
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            max_count = max(d.values())
            
            while (j-i+1) - max_count > k:
                   d[s[i]]-=1
                   i+=1
            l=max(l,j-i+1)
            j+=1
        return l
               
