class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        seen=set()
        def helper(path,seen):
            if len(path)==len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if nums[i] in seen: 
                    continue
               
                path.append(nums[i])
                seen.add(nums[i])
                helper(path,seen)

                a=path.pop()
                seen.discard(a)

        helper([],seen)
        return res
                
                
                

