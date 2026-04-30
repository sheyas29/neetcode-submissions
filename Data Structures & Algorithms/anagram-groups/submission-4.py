from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        e_result=[]
        for i in range(0,len(strs)):
            i_result=[]
            if any(strs[i] in inner for inner in e_result):
               continue
            else: i_result.append(strs[i])
            for j in range(i+1,len(strs)):
                if any(strs[j] in inner for inner in e_result) :
                    continue
                elif Counter(strs[i])==Counter(strs[j]):
                    i_result.append(strs[j])
            e_result.append(i_result)
            
            
        return e_result


        