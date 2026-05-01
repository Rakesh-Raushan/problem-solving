class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #[a,b] > a is dependent on b b->a graph wise
        #[0,1] 1 before 0
        #course 0 to numCourses - 1
        #let's see if we can get the courses ordered in topological manner
        #if so we can say True else False
        #any course which does not depend on a course can be taken 
        in_degree = [0]*numCourses
        adj = {i : [] for i in range(numCourses)}
        #{0: [], 1:[0],}
        #[1,0]
        for course, pre_course in prerequisites:
            adj[pre_course].append(course)
            in_degree[course]+=1
        
        #put all zero in degree courses in a queue
        from collections import deque
        queue = deque([i for i in range(numCourses) if in_degree[i]==0])

        toposort = []
        while queue:
            course = queue.popleft()
            toposort.append(course)

            for dep_course in adj[course]:
                in_degree[dep_course]-=1
                if in_degree[dep_course] ==0:
                    queue.append(dep_course)
        
        return len(toposort) == numCourses



        