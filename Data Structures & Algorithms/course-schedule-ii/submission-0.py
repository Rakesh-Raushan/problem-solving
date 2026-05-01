class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #clearly topological sorting or courses is required
        #let's do in BFS style using Kahn algo

        #create adj list and a indeg array or prerequisites array
        adj = {i:[] for i in range(numCourses)}
        prereq_count_list = [0]*numCourses
        for c1,c2 in prerequisites:
            adj[c2].append(c1)
            prereq_count_list[c1]+=1

        valid_course_order = []

        #initialize queue with all zero indeg nodes
        from collections import deque
        queue = deque([i for i in range(numCourses) if prereq_count_list[i]==0]) #no prereq courses

        while queue:
            #pop FIFO manner and zero indeg nodes/course can be appended to result
            no_prereq_course = queue.popleft()
            #append to valid order
            valid_course_order.append(no_prereq_course)
            
            for rel_course in adj[no_prereq_course]:
                #update the graph neighbours in terms of indeg array after removing the zero indeg node
                prereq_count_list[rel_course]-=1
                #check if its neighbour has become zero deg in the process, if so add it to queue to be processed
                if prereq_count_list[rel_course] == 0:
                    queue.append(rel_course)
        
        #check if all nodes processed in the result if not return blank else result
        return valid_course_order if len(valid_course_order) == numCourses else []

#verify: numCourses = 3, prerequisites = [[1,0]] Output: [0,1,2]
#adj = {0:[1], 1: [], 2: []}, prereq_count = [0, 1, 0], valid course order = []
#queue = [0,2]
#valid course order = [0], rel course = 1, queue = [2,1]
#valid course order = [0,2] queue = [1]
#valid course order = [0,2,1] queue = []
#len = 3 = Num courses

        