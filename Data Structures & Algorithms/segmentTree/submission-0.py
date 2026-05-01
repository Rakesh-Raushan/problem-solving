class SegmentTreeNode:
    def __init__(self, total, L, R):
        self.total = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None
    
    @staticmethod
    def build(nums, L, R):
        #base case:
        if L == R:
            return SegmentTreeNode(nums[L],L,R)
        
        #if not the case of leaf node
        M = (L+R)//2

        #create a root node, with initially assuming total as 0, which we update later based on left and right child
        root = SegmentTreeNode(0,L,R)
        #now build the left and right of this root again assuming their sums to be 0 which we later update
        root.left = SegmentTreeNode.build(nums,L,M)
        root.right = SegmentTreeNode.build(nums,M+1,R)

        #update the sum based on these
        root.total = root.left.total + root.right.total

        return root
    
    def _update(self, index: int, val: int) -> None:
        #base case
        if self.L == self.R == index:
            self.total = val
            return
        # else go to that leaf node
        M = (self.L+self.R)//2

        #target in left tree
        if index <=M:
            self.left._update(index, val)
        else:
            #target in right tree
            self.right._update(index, val)
        
        # also update the sum
        self.total = self.left.total + self.right.total
        return

    def _query(self, L: int, R: int) -> int:
        #base case the current node is the range being queried
        if self.L==L and self.R==R:
            return self.total

        #if not so check if the left tree completely covers the range queried
        M = (self.L+self.R)//2

        if R<=M:
            #query the left tree
            return self.left._query(L,R)
        elif L>M:
            #query the right tree
            return self.right._query(L,R)
        else:
            #query range overlaps both left and right subtrees
            return (self.left._query(L,M) + self.right._query(M+1,R))

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = SegmentTreeNode.build(nums, 0, len(nums)-1)
    
    def update(self, index: int, val: int) -> None:
        return self.root._update(index,val)

    def query(self, L: int, R: int) -> int:
        return self.root._query(L,R)