class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        n = len(prices)
        if n == 1:
            return 0
        ans = max(0, prices[j] - prices[i])
        while i < j and j < n:
            if prices[j] > prices[i]:
                ans = max(ans, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return ans