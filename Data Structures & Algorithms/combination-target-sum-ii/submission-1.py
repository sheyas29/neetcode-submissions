class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sorting is the key to O(1) duplicate detection
        candidates.sort()

        def backtrack(start_index, path, remaining_target):
            # Base Case: Success
            if remaining_target == 0:
                res.append(list(path))
                return
            
            # Iterate through candidates starting from the current index
            for i in range(start_index, len(candidates)):
                # OPTIMIZATION 1: Pruning
                # If the current number is greater than what we need, 
                # all subsequent numbers will also be too big (since array is sorted)
                if candidates[i] > remaining_target:
                    break
                
                # OPTIMIZATION 2: Skip Duplicates
                # If this number is the same as the previous one in THIS loop level, skip it.
                # 'i > start_index' ensures we can still pick duplicate numbers 
                # from DIFFERENT levels (e.g., [2, 2] is allowed if we have two 2s)
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Standard Backtracking steps:
                path.append(candidates[i])
                # Move to i + 1 because each element can only be used once
                backtrack(i + 1, path, remaining_target - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res