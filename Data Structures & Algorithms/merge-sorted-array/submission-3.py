from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        end = m                      # index just past the real elements in nums1

        while j < n and i < end:
            if nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                end += 1             # nums1 grew, so the boundary moved right
            else:
                i += 1

        nums1[i:i] = nums2[j:]       # leftovers from nums2 (all >= every real element)
        del nums1[m + n:]            # drop the extra zeros pushed to the end