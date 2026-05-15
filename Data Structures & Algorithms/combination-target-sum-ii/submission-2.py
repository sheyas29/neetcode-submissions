class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # Still essential for the logic to work

        def backtrack(start_index, path, curr_sum):
            # Base Case: Success
            if curr_sum == target:
                res.append(list(path))
                return
            
            # Iterate through the available candidates
            for i in range(start_index, len(candidates)):
                # OPTIMIZATION: Early Exit (Pruning)
                # Since the list is sorted, if adding the current number 
                # puts us over the target, all numbers after it will too.
                if curr_sum + candidates[i] > target:
                    break
                
                # SKIP DUPLICATES:
                # If this number is the same as the one we just tried 
                # for this 'position' in the combination, skip it.
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Inclusion
                path.append(candidates[i])
                # Recurse: move to i + 1 to ensure each element is used only once
                backtrack(i + 1, path, curr_sum + candidates[i])
                # Backtrack: remove the number to try the next iteration
                path.pop()

        backtrack(0, [], 0)
        return res