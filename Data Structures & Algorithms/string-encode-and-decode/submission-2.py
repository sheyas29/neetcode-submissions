class Solution:

    def encode(self, strs: List[str]) -> str:
        r=""
        for s in strs:
            r+=(str(len(s))+"#"+s)
        return r



    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
    
        while i < len(s):
            word=[]
            j=i
            length_str=""
            while j<len(s):
                if s[j]!='#':
                   length_str+=(s[j])
                   j+=1
                else:break
            word=s[i+len(length_str)+1:i+len(length_str)+1+int(length_str)]
            result.append(word)
            i=i+len(length_str)+int(length_str)+1
       
        return result