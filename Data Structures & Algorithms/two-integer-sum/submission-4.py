from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(list)
        res=[]
        for i,n in enumerate(nums):
            if target-n in seen and seen[target-n]!=i:
                return [seen[target-n],i]
            seen[n]=i
            
        return []