class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        i=0
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False