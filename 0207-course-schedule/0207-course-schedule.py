class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap={i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            cmap[crs].append(pre)

        visited=set()

        def dfs(crs):
            if crs in visited:
                return False
            if cmap[crs]==[]:
                return True

            visited.add(crs)
            for pres in cmap[crs]:
                if not dfs(pres):
                    return False
            visited.remove(crs)

            cmap[crs]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        