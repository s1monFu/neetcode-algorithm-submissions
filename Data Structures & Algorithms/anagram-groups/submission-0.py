class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        maps = []
        for s in strs:
            ha = {}
            for c in s:
                ha[c] = 1 + ha.get(c, 0)
            found = False
            for i, ma in enumerate(maps):
                if ha == ma:
                    ans[i].append(s)
                    found = True
                    break
            if not found:
                ans.append([s])
                maps.append(ha)
        return ans

                