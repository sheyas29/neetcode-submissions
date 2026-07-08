class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            if nums[i] == val:
                if nums[j] == val:
                    # Both are 'val'. Just shrink the right pointer.
                    j -= 1
                else:
                    # Swap the 'val' at i with the valid number at j.
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            else:
                # Left element is already valid. Move forward.
                i += 1
                
        return i
