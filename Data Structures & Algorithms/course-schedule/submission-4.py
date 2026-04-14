class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        matrix = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            matrix[a].append(b)
        
        visiting = set()

        def dfs(cur):
            if cur in visiting:
                return False
            visiting.add(cur)
            for b in matrix[cur]:
                if not dfs(b):
                    return False
            visiting.remove(cur)
            # matrix[cur] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True