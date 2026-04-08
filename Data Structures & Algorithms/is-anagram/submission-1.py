class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        for x in s:
            if x not in ss:
                ss[x] = 1
            else:
                ss[x] += 1
        for y in t:
            if y not in ss:
                return False
            if ss[y] == 0:
                return False
            ss[y] -= 1
        for x in ss:
            if ss[x] > 0:
                return False
        return True

        