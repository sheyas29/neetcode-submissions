class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(index,path):
            if index>=len(nums):
                res.append(list(path))
                return
            
            path.append(nums[index])
            backtrack(index+1,path)

            path.pop()
            
            while index+1 < len(nums) and nums[index+1]==nums[index]:
                index+=1
                continue
            backtrack(index+1,path)

        backtrack(0,[])
        return res

            