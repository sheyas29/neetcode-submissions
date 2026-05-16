class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(path,o,c):
            if o==0 and c==0:
                res.append(''.join(path))
                return

            
            if c>0:
                path.append(')')
                helper(path,o,c-1)
                a=path.pop()
                   
            if o>0 and o<c:
                path.append('(')
                helper(path,o-1,c)
                a=path.pop()
                   
            if o==c:
                path.append('(')
                helper(path,o-1,c)
                a=path.pop()
                
            
        helper([],n,n)
        return res
                

