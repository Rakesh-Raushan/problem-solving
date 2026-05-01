class TimeMap:

    # def __init__(self):
    #     self.key_val_store = dict()    

    # def set(self, key: str, value: str, timestamp: int) -> None:
    #     timestamp_idx = timestamp
    #     if key in self.key_val_store:
    #         val_at_prev_timestamp = self.key_val_store[key][-1]
    #         last_timestamp_idx = len(self.key_val_store[key])-1
    #         while(timestamp_idx - last_timestamp_idx>1):
    #             last_timestamp_idx+=1
    #             self.key_val_store[key].append(val_at_prev_timestamp)
    #         self.key_val_store[key].append(value)
    #     else:
    #         if timestamp > 0:
    #             self.key_val_store[key] = [""]*(timestamp)
    #             self.key_val_store[key].append(value)
    #         else:
    #             self.key_val_store[key]=[value]

    # def get(self, key: str, timestamp: int) -> str:
    #     val_arr = self.key_val_store.get(key,[""])
    #     if len(val_arr) < timestamp:
    #         return val_arr[-1]
    #     else:
    #         return val_arr[timestamp-1]

    #above is actually correct and works although needtcode has a wrong testcase of timestamp 0 which is not as per given constraints so fails
    #but besides, this is not a good solution in terms of space constraint, the list creates a lot of repeated vals {key: [val, val,val ,...val]}
    #better solution to store as {key: [(timestamp, val) ,...val]}, i.e list of tuple and then search timestamp as binary as we know they will be set in
    # increasing order and if it is not found then return last val and if no value then ""
    from collections import defaultdict
    def __init__(self):
        self.key_val_store = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        # we will maintain a tuple as value (timestamp, value)
        self.key_val_store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.key_val_store[key]
        #if the val_list is empty return ""
        if len(val_list)==0:
            return ""

        #since the timestamps will be in sorted order, let's apply a binary search on this list
        left, right = 0, len(val_list)-1
        while(left <=right):
            mid = (left + right)//2
            if timestamp == val_list[mid][0]:
                return val_list[mid][1]
            elif timestamp > val_list[mid][0]:
                left = mid+1
            else:
                right = mid-1
        #if the timestamp is not found but the val_list is non empty, return lower timestamp val if it exists
        #when timestamp is not there in the list, the end of loop will happen with left >right with either right <0 or left =len(val_list) | since we 
        #the value will be out of range in the sense it will be either lower than lowest or bigger than biggest val in list
        # no but it is possible a value in middle might also be not there, e.g 2,5,6,8,12 target3, we need to return 2, target 9 we need to return 8
        #so if it is outside bounday we can return "" if it is lower than lowest timestamp and we can return val_list[-1][1] if bigger than biggest
        #if it is in middle and left>right case, e.g 2,5,7,8,12 target3, left=1, right=0 will be the case, case target is 6,left=2,right=1,
        #actually whenever it will be in middle, the left right will equate to the num just lower than it and then left will become>right at break of loop
        #so right will give the index of the num just lower than target
        print(f"val_list:{val_list}, left:{left} , right:{right}")
        #lower boundary crossed
        if right < 0:
            return ""
        #upper boundary crossed or middle both cases we can depend on right pointer at loop exit
        else:
            return val_list[right][1]
        

        
