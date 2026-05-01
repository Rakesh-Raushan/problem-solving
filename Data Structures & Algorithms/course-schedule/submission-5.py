class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #let;s take the approach of topological sorting with BFS (Kahn's algo)
        # from collections import defaultdict, deque
        course_graph = {i:[] for i in range(numCourses)}
        #course dependency count
        course_dep = [0]*numCourses
        for c1, c2 in prerequisites:
            course_graph[c2].append(c1)
            course_dep[c1]+=1
        
        queue = deque([i for i in range(numCourses) if course_dep[i]==0]) #no dependency courses

        toposort_courses = []
        while queue:
            independent_course = queue.popleft()
            toposort_courses.append(independent_course)

            #update neighbours considering this one as removed from course graph
            for dep_course in course_graph[independent_course]:
                course_dep[dep_course]-=1
                if course_dep[dep_course] == 0:
                    #became independent, can be processed
                    queue.append(dep_course)
        #if all courses got topologically sorted then courses cana be taken else not
        return len(toposort_courses)==numCourses

#verify numCourses = 2, prerequisites = [[0,1]]
#course graph={0:[],1:[0]}, course dep = [1,0], queue = [1]
#ind course 1, topsort=[1],dep_course = 0, course dep = [0,0] queue = [0]
#ind course 0, topsort = [1,0] dep_course = None so over
#[1,0] has 2 ele so true

        
        