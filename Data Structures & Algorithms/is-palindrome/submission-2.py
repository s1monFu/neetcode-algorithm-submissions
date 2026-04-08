class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n and not s[i].isalnum() :
            i += 1
        j = n-1
        while j >= 0 and not s[j].isalnum() :
            j -= 1
        while i <= j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            while i < n and not s[i].isalnum() :
                i += 1
            j -= 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
        return True