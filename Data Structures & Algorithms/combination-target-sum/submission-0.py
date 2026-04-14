class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []
        total = 0
        def dfs(i):
            nonlocal total, combination
            if total == target:
                ans.append(combination.copy())
                return
            if total > target or i >= len(nums):
                return
            
            total += nums[i]
            combination.append(nums[i])
            dfs(i)
            total -= nums[i]
            combination.pop()
            dfs(i+1)
        
        dfs(0)
        return ans
                
            