class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        d={}
        while i<len(nums):
            d[nums[i]]=i
            i+=1
            if target-nums[i] in d:
                return [d[target-nums[i]],i]
    
            
        return None