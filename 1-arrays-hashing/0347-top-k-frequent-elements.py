import heapq

from typing import List

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = dict()
        heap = []

        for n in nums:
            if n in countMap:
                countMap[n] = countMap[n] + 1
            else:
                countMap.update({ n: 1 })

        for n, c in countMap.items():
            if len(heap) < k:
                heapq.heappush(heap, [c, n])
            else:
                heapq.heappushpop(heap, [c, n])

        return [pair[1] for pair in heap]
