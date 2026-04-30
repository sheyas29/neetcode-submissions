class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Counting machine: number → how many
        counts = Counter(nums)          # O(n)

    # 2. Make prize shelves: shelf 3 holds all numbers seen 3 times
        shelf = [[] for _ in range(len(nums)+1)]
        for num, freq in counts.items():# O(n)
            shelf[freq].append(num)

    # 3. Walk backwards on shelves, grab k trophies
        trophies = []
        for f in range(len(shelf)-1, 0, -1):  # start at highest shelf
            trophies.extend(shelf[f])
            if len(trophies) >= k:
               return trophies[:k]