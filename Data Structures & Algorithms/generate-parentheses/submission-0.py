class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(i, j, cur):
            if i == j == n:
                ans.append("".join(cur))
            if i < n:
                cur.append("(")
                i += 1
                dfs(i, j, cur)
                cur.pop()
                i -= 1
            if j < i:
                cur.append(")")
                j += 1
                dfs(i, j, cur)
                cur.pop()
                j -= 1
        dfs(0,0, [])
        return ans


