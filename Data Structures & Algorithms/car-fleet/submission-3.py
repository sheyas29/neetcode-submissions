from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        check = dict()
        stack=[]
        for i in range(len(position)):
            check[position[i]]=speed[i]
        check = dict(sorted(check.items(), reverse=True))
        for k,v in check.items():
            t=(target-k)/v
            print(t)
            if stack and stack[-1]>=t:
                continue
            stack.append(t)      
        return len(stack)