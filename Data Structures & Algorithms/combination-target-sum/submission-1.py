class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(path,index,curr_sum):
            if curr_sum==target:
                res.append(list(path))
                return
            if index>=len(nums) or curr_sum>target:
                return
            path.append(nums[index])
            curr_sum+=nums[index]
            helper(path,index,curr_sum)

            path.pop()
            curr_sum-=nums[index]
            helper(path,index+1,curr_sum)
        helper([],0,0)
        return res