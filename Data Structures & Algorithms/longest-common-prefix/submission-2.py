class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        curr = list(strs[0])
        res=curr
        for i in range(1,len(strs)):
            j=0
            check = list(strs[i])
            while j<len(curr):
                if check[j]!=curr[j]:
                    res=curr[:j]
                    break
                j+=1
            curr=res
        return "".join(res)