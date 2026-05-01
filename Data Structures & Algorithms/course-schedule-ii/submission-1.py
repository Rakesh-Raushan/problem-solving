class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #topological sorting can help us here
        #idea i can use is any course without any prerequisites can be taken, once that is
        #taken, some course which depended on just this can now be taken and so on.
        
        adj = {i: [] for i in range(numCourses)}
        num_prereq = [0]*numCourses

        for course, pre_course in prerequisites:
            adj[pre_course].append(course)
            num_prereq[course]+=1
        
        #we will take a bfs approach
        from collections import deque
        queue = deque([i for i in range(numCourses) if num_prereq[i]==0])

        topo_order = []
        while queue:
            pre_course = queue.popleft()
            topo_order.append(pre_course)

            for course in adj[pre_course]:
                num_prereq[course]-=1
                if num_prereq[course]==0:
                    queue.append(course)
        
        return topo_order if len(topo_order)==numCourses else []

