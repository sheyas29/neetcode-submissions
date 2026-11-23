from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        window = defaultdict(int)
        window[nums[i]]=i
        for j in range(1,len(nums)):
            if j-i > k :
                del window[nums[i]]
                i+=1
            if nums[j] in window:
                return True    
            window[nums[j]]=j
        return False