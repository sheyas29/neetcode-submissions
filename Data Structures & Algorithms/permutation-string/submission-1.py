from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        j=0
        check=Counter(s1)
        length=len(s1)
        d={}
        if len(s2)<len(s1):
            return False
        while j<len(s2):
            while (j-i+1) <= length:
                d[s2[j]] = d.get(s2[j],0)+1
                if d==check:
                    return True
                j+=1
            if d[s2[i]]==1:
                del d[s2[i]]
                i+=1
            else :
                d[s2[i]]-=1
                i+=1
        return False
            
                