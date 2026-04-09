class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for c in s:
            if c not in hashmap:
                ls.append(c)
                continue

            if ls and ls[-1] == hashmap[c]:
                x = ls.pop()
            else:
                ls.append(c)
        return len(ls) == 0