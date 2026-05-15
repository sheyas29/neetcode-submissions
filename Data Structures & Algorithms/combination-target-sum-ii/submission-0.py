class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def helper(path,index,curr_sum):
            if curr_sum==target:
                res.append(list(path))
                return
            if index>=len(candidates) or curr_sum>target:
                return
            path.append(candidates[index])
            
            
            helper(path,index+1,curr_sum+candidates[index])

            path.pop()
            next_index = index+1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            helper(path,next_index,curr_sum)
        helper([],0,0)
        return res

            
