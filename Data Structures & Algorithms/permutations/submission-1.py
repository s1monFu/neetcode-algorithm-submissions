class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(cur, nums, pick):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    cur.append(nums[i])
                    pick[i] = True
                    dfs(cur, nums, pick)
                    cur.pop()
                    pick[i] = False
        dfs([], nums, [False] * len(nums))
        return ans
        