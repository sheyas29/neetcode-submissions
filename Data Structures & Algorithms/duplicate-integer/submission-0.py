class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        n=len(nums)
        i=0
        j=1
        while i<n and j<n:
            if nums[i]==nums[j]:
               return True
            i+=1
            j+=1
        return False
    