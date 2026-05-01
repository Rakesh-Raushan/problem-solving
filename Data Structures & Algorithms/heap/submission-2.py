class MinHeap:
    
    def __init__(self):
        self.heap = [0] #arr of dummy zero index (for 2i left adn 2i+1 right child)
        

    def push(self, val: int) -> None:
        # in push we do two things,
        # first, we put new node as last node to maintain the structure of complete BT
        # needed for a heap and filling left to right
        # then we ensure the order property by percolating this new node up, till
        # we see the condition, node < its left and right subtree is valid

        #step1
        self.heap.append(val)

        #step2
        i = len(self.heap)-1
        # while parent is there, and parent is greater than both the children,
        # swap with smaller
        while(i//2>0): 
            if self.heap[i//2] > self.heap[i]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2

    def pop(self) -> int:
        # in pop we first need to replace top with last and then percolate down from top

        #step 1
        if len(self.heap)==1:
            return -1
        if len(self.heap)==2:
            return self.heap.pop()
        
        res = self.heap[1]

        self.heap[1] = self.heap.pop()

        i = 1# percolate down from the first node

        #while the left child for a node exists (if left not there no right for complete BT)
        while(2*i<len(self.heap)):
            if(2*i+1<len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[2*i+1] < self.heap[i]):
                # if right exists and right is smaller than left and right less than parent
                #swap with right
                self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                #update the i
                i = 2*i+1
            elif self.heap[2*i] < self.heap[i]:
                #swap with left
                self.heap[2*i], self.heap[i] = self.heap[i], self.heap[2*i]
                #update i
                i = 2*i
            else:
                #no need for any further percolation
                break
        
        return res

    def top(self) -> int:
        if len(self.heap)==1:
            return -1
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        if len(nums)<=1:
            return
        # get the array with dummy zero
        self.heap = nums
        self.heap.append(self.heap[0])

        #skip leaf from right
        cur = (len(self.heap)-1)//2

        while(cur>0):
            i = cur
            #while the left child for a node exists (if left not there no right for complete BT)
            while(2*i<len(self.heap)):
                if(2*i+1<len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[2*i+1] < self.heap[i]):
                    # if right exists and right is smaller than left and right less than parent
                    #swap with right
                    self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                    #update the i
                    i = 2*i+1
                elif self.heap[2*i] < self.heap[i]:
                    #swap with left
                    self.heap[2*i], self.heap[i] = self.heap[i], self.heap[2*i]
                    #update i
                    i = 2*i
                else:
                    #no need for any further percolation
                    break
            cur-=1

        
        