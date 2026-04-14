class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []
        total = 0
        def dfs(i):
            nonlocal total
            if i >= len(nums) or total > target:
                return
            
            total += nums[i]
            combination.append(nums[i])
            if total == target:
                ans.append(combination.copy())
            dfs(i)
            combination.pop()
            total -= nums[i]
            dfs(i+1)
        dfs(0)
        return ans
                
            