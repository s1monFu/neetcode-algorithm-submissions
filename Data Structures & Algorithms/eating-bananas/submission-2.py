class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ma = max(piles)
        i = 1
        j = ma
        ans = ma
        while i <= j:
            mid = (i + j) // 2
            cnt = sum(-(-x // mid) for x in piles)
            # print(f"i: {i}, j: {j}, mid: {mid}, cnt: {cnt}")
            if cnt > h:
                i = mid + 1
            elif cnt <= h:
                j = mid - 1
                ans = min(ans, mid)
        return ans
        