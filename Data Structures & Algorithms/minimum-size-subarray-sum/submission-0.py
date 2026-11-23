class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        i=0
        curr_sum=0
        curr_len=0
        for j in range(len(nums)):
            curr_sum+=nums[j]
            
            while curr_sum>=target:
                curr_len=j-i+1
                minlen = min(minlen,curr_len)
                curr_sum-=nums[i]
                i+=1
            
        return minlen if minlen!=float('inf') else 0    

