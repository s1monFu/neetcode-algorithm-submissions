class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10000000
        cur = 0
        for x in nums:
            cur += x
            ans = max(ans, cur)
            if cur < 0:
                cur = 0
        return ans
