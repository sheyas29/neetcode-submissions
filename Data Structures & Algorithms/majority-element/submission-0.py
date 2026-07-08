from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans=0
        for k,v in count.items():
            if v>len(nums)/2:
                ans = k
        return ans