class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.minHeap = [[x*x + y*y, x, y] for x, y in points]
        heapq.heapify(self.minHeap)
        
        ans = []
        while k > 0:
            k -= 1
            l, x, y = heapq.heappop(self.minHeap)
            ans.append([x,y])
        
        return ans