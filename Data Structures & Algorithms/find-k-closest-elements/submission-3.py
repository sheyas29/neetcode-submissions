from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        while i + k < len(arr) and x - arr[i] > arr[i + k] - x:
            i += 1
        return arr[i:i + k]