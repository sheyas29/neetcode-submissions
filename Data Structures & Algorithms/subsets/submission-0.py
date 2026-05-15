class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(index,path):
            if index==len(nums):
                res.append(list(path))
                return
            
            path.append(nums[index])
            helper(index+1,path)

            path.pop()
            helper(index+1,path)

        helper(0,[])
        return res
            