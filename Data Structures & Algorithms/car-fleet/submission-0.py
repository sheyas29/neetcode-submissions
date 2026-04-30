from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position and speed, then sort by position descending
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        stack: List[float] = []
        
        for pos, spd in cars:
            t = (target - pos) / spd  # time to reach target
            # If this car reaches later than the fleet ahead, it becomes a new fleet
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)