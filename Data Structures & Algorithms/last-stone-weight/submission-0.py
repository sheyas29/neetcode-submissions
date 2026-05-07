class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            y=heapq.heappop_max(stones)
            x=heapq.heappop_max(stones)
            if x == y:
                continue
            elif x < y:
                y=y-x
                heapq.heappush_max(stones,y)
        if not stones:
            return 0
        else:
            return stones[0]