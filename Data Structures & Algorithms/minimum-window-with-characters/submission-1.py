class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check=Counter(t)
        d=Counter({})
        l_min=float('inf')
        i=0
        j=0
        res={}
        inv={}
        if len(t)>len(s):
            return ""
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            while check <=d:
                if s[i] not in check:
                    if d[s[i]]==1:
                        del d[s[i]]
                    else:
                        d[s[i]]-=1
                    
                elif s[i] in check:
                    
                    if d[s[i]]==1:
                        del d[s[i]]
                    else:
                        d[s[i]]-=1
                if j-i+1 < l_min:
                    l_min=min(l_min,j-i+1)
                    res[s[i:j+1]]=l_min
                i+=1
            j+=1
        if l_min == float('inf'):
            return ""
        inv = {v: k for k, v in res.items()}
        return inv[l_min]