class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            
            j=i+1
            print(i,j)
            while j<len(temperatures) and temperatures[i]>=temperatures[j]:
                print(f'i={i}, j={j}')
                print(f'{temperatures[i]}=>{temperatures[j]},contniue')
                j+=1

            if j<len(temperatures) and temperatures[i]<temperatures[j]:
                print(f'i={i}, j={j}')
                print(f'{temperatures[i]}<{temperatures[j]}, found warmer temperature')
                res[i]=j-i
                print(res)
        return res
            
            
            
            
            
