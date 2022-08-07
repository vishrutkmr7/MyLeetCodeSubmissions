class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            d[course].append(prereq)
        
        visit, cycle = set(), set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for nei in d[course]:
                if not dfs(nei):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output