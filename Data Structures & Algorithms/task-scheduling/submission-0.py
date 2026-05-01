class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #general idea is to prioritise tasks with higher count and set aside the instances of tasks scheduled until the idle time passes
        # we can use a heap to repeatedly pick tasks with highest freq at any time
        # we can also set aside tasks with the time information, when can they be scheduled next in a queue
            # queue bcoj tasks waiting longest will be eligible the first, so FIFO can help us here
        #after each iteration (passage of one unit time, we will check if the longest waiting task in queue is eligible for scheduling
        # if so we wil bring it back to our heap
        #since we need to schedule all the tasks we will run the loop till the heap and queue both are exhausted through iteration
        # after exhaustion, we will get the time required min (the number of iterations) for scheduling all the tasks

        from collections import Counter, deque
        task_counts = Counter(tasks)

        #we create a maxheap using this but only of the times as our aim to find the time
        count_maxheap = [-c for c in task_counts.values()] # neg to simulate maxheap using python minheap

        #heapify it
        heapq.heapify(count_maxheap)

        #take a queue for waiting task
        tasks_waiting = deque()

        #set starting time to zero
        time = 0

        #iterate to cover all tasks across heap and queue
        while count_maxheap or tasks_waiting:
            #increase time by 1 for every iter
            time+=1

            #if tasks in our heap
            if count_maxheap:
                #get the task with max count and simulate scheduling by reducing its count by 1
                count = heapq.heappop(count_maxheap) + 1 # +1 instead of -1 since we added -counts to simulate maxheap using python minheap
                #if we still have count for the tasks, they must wait till time becomes curr time + waiting time and from next iter they will be eligible
                #so send them to waiting queue
                if count:
                    tasks_waiting.append((count, time + n))
            
            #check if waiting queue has tasks and if so if the longest waiting task index 0 next time matches curr time
            #they can be considered for scheduling in the next iter
            if tasks_waiting and tasks_waiting[0][1] == time:
                #this task has now become eligible for scheduling as its waiting time has passed so lets add it back to maxheap
                heapq.heappush(count_maxheap, tasks_waiting.popleft()[0])
        
        #after the loop return the time as the time needed to finish all times in the min time manner
        return time
        