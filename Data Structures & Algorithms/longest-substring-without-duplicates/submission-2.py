class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        i = 0
        j = 1
        n = len(s)
        if n == 0 or n == 1:
            return n
        hashmap[s[i]] = 1
        ans = 0
        while j < n:
            while i < j and s[j] in hashmap:
                del hashmap[s[i]]
                i += 1
            ans = max(ans, j - i + 1)
            hashmap[s[j]] = 1
            j += 1
        return ans