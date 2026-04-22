class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        i = 0
        j = -1
        m = len(matrix)
        n = len(matrix[0])
        curdi = 0
        total = m* n
        while len(res) < total:
            dx, dy = dir[curdi]
            for _ in range(n):
                i += dx
                j += dy
                res.append(matrix[i][j])
                
            curdi = (curdi+1)%4
            n, m = m - 1, n
            
        return res