class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        curr = list(strs[0])
        res=curr
        for i in range(1,len(strs)):
            print(f'i=>{i}')
            j=0
            check = list(strs[i])
            print(check,curr)
            while j<len(curr):
                print(check[j],curr[j])
                if check[j]!=curr[j]:
                    res=curr[:j]
                    print(f'reduced=>{res}')
                    break
                j+=1
            curr=res
            print(curr)
        return "".join(res)