class Solution:
    def countBits(self, n: int) -> List[int]:
        cnts = []
        for i in range(n+1):
            one = 0
            for _ in range(32):
                if i & (1 << _):
                    one += 1
            cnts.append(one)
        return cnts