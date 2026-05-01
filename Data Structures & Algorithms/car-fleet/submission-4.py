class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # #based on position we can have an array of distance to target
        # dist_to_target = [target - x for x in position]

        # #based on speed we can have array of time taken to cover
        # time_to_reach = [dist//speed for dist,speed in zip(dist_to_target, speed)]

        # return len(set(time_to_reach))

    #verify: target = 10, position = [1,4], speed = [3,2]
    # dist_to_target = [9,6], time_to_reach = [9//3,6//2] = [3,3] set = {3}, len =1 correct
    #verify: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
    # dist_to_target = [6,9,10,3], time_to_reach = [3,4,10,3], set = {3,4,10}, len =3 correct
    #verify: target=12 position=[10,8,0,5,3] speed=[2,4,1,1,3]
    #dist_to_target = [2,4,12,7,9], time_to_reach = [1,1,12,7,3] ans = 4
    # the above solution ignore the order of cars completely and also the fact that overtake wont happen
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #so to ensure that we do not allow overtake and take care of order
        #first we order the car and then populate the time to reach
        #further if any car ahead to curr  has time to distance more than is it, means the curr car will form a fleet
        # so we can maintain the time to distance in a monotonic manner for the correct count
        
        #combined pos and speed array
        position_speed = [(position, speed) for position, speed in zip(position, speed)]
        #order by position
        position_speed.sort(key=lambda x: x[0])

        #fleet stack, based on monotonically decreasing time, can also first calculate time and then do the monotonic thing
        fleet_stack = []

        for cur_position, cur_speed in position_speed:
            cur_time_to_dest = round((target - cur_position)/cur_speed, 3) #assuming this much pos comparision
            while fleet_stack and cur_time_to_dest >= fleet_stack[-1]:
                fleet_stack.pop()
            fleet_stack.append(cur_time_to_dest)
        #fleet_stack will consist of times of fleets, so num of fleets = len of fleet_stack
        return len(fleet_stack)
        
        #verify: target=12 position=[10,8,0,5,3] speed=[2,4,1,1,3]
        #position_speed = [(10,2),(8,4),(0,1),(5,1),(3,3)]
        #sorted position_speed = [(0,1),(3,3),(5,1),(8,4),(10,2)]
        #fleet stack=[],>(0,1)> 12, stack = [12]
        #>(3,3)>3, stack = [12,3]
        #>(5,1)>7, stack = 7>3 so pop, 7<12 so no pop, then push so stack = [12,7]
        #>(8,4)>1, stack =1<7 no pop so stack = [12,7,1]
        #>(10,2), 1 1==1 so pop and 1<7 so push so stack = [12,7,1]
        #loop over, return 3 , Works!!

