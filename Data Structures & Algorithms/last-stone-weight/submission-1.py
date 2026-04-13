class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-x for x in stones]
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > 1:
            a = heapq.heappop(self.maxHeap)
            b = heapq.heappop(self.maxHeap)
            a = -a
            b = -b
            if a == b:
                continue
            if a < b:
                heapq.heappush(self.maxHeap, -(b - a)) 
            else:
                heapq.heappush(self.maxHeap, -(a-b)) 

        return -self.maxHeap[0] if len(self.maxHeap) > 0 else 0