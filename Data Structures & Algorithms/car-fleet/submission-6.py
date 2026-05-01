from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        check = sorted(zip(position, speed), reverse=True)
        for k,v in check:
            t=(target-k)/v
            if stack and stack[-1]>=t:
                continue
            stack.append(t)      
        return len(stack)