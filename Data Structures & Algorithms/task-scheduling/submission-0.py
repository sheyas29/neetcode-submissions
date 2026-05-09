import heapq

from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        
        # max heap (negative values)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)
        
        time = 0
        
        while max_heap:
            temp = []
            cycle = 0
            
            # process up to n+1 tasks
            for _ in range(n + 1):
                if max_heap:
                    cnt = heapq.heappop(max_heap)
                    if cnt + 1 < 0:   # still remaining
                        temp.append(cnt + 1)
                    cycle += 1
                else:
                    break
            
            # push remaining tasks back
            for item in temp:
                heapq.heappush(max_heap, item)
            
            # if heap still has tasks → full cycle
            if max_heap:
                time += (n + 1)
            else:
                time += cycle
        
        return time

            