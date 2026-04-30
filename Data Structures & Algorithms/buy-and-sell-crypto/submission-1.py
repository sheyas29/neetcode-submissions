class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        max_diff=0
        while j<len(prices):
            if prices[i]>=prices[j]:
                i=j
            
            else:
                max_diff=max(max_diff,prices[j]-prices[i])
            j+=1
        return max_diff
