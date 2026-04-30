class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        j=k
        res=[]
        while j<len(nums)+1:
            max_e=max(nums[i:j])
            res.append(max_e)
            i+=1
            j+=1
        return res