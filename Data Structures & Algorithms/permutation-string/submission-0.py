class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for c in s1:
            hashmap[c] = 1 + hashmap.get(c, 0)
        n1 = len(s1)
        n2 = len(s2)
        i = 0
        j = n1 - 1
        while j < n2:
            if sorted(s1) == sorted(s2[i:j+1]):
                return True
            i += 1
            j += 1
        return False

